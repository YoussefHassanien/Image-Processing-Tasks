import cv2
import numpy as np
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class ImageProcessor:
    def __init__(self, ui):
        self.ui = ui
        self.original_images = [None, None]  # For storing original images
        self.harris_image = None  # For harris corner detection
        self.dft_components = [None, None]  # For storing DFT components
        self.magnitudes = [None, None]      # For storing magnitude components
        self.phases = [None, None]          # For storing phase components
        self.output_window = None           # Reference to output window

    def update_k_value(self):
        """Update LCD display with current k value"""
        k_value = self.ui.k_slider.value() / 1000.0
        self.ui.k_value_LCD.display(k_value)
    
    def load_image(self, index):
        """Load image for specified slot (0 or 1)"""
        file_path, _ = QFileDialog.getOpenFileName(
            None, f"Open Image {index+1}", "", 
            "Images (*.png *.jpg *.jpeg *.bmp *.tif);;All Files (*)"
        )
        
        if file_path:
            # Read image in color
            image = cv2.imread(file_path)
            if image is None:
                QtWidgets.QMessageBox.warning(None, "Error", "Could not open image!")
                return
                
            # Store original image
            self.original_images[index] = image
            
            # Convert BGR to RGB for display
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Display in appropriate view
            if index == 0:
                self.ui.Image_1.setImage(np.transpose(rgb_image, (1, 0, 2)))
            else:
                self.ui.Image_2.setImage(np.transpose(rgb_image, (1, 0, 2)))
            
            # Compute DFT components
            self.compute_dft_components(image, index)
    
    def compute_dft_components(self, image, index):
        """Compute magnitude and phase components of DFT for an image"""
        # Convert to grayscale if needed
        if len(image.shape) > 2:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
            
        # Apply DFT
        dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        
        # Compute magnitude spectrum
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)
        
        # Normalize magnitude for display
        magnitude_display = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        # Compute phase
        phase = cv2.phase(dft_shift[:, :, 0], dft_shift[:, :, 1])
        phase_display = cv2.normalize(phase, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        # Store components
        self.magnitudes[index] = magnitude_spectrum
        self.phases[index] = phase
        
        # Store complex DFT for reconstruction
        self.dft_components[index] = dft_shift
        
        # Determine which component to display
        component_choice = self.ui.Image1_component_comboBox.currentIndex() if index == 0 else self.ui.Image2_component_comboBox.currentIndex()
        component_display = magnitude_display if component_choice == 0 else phase_display
        
        # Display the component
        if index == 0:
            self.ui.Image1_component.setImage(np.transpose(component_display, (1, 0)))
        else:
            self.ui.Image2_component.setImage(np.transpose(component_display, (1, 0)))
    
    def mix_components(self):
        """Mix components from both images based on selected options and sliders"""
        # Check if both images are loaded
        if any(img is None for img in self.original_images):
            QtWidgets.QMessageBox.warning(None, "Error", "Please load both images first!")
            return
            
        # Get component selection for each image
        comp1_index = self.ui.Image1_component_comboBox.currentIndex()  # 0 = magnitude, 1 = phase
        comp2_index = self.ui.Image2_component_comboBox.currentIndex()  # 0 = magnitude, 1 = phase
        
        # Check if we have valid combinations
        if comp1_index == comp2_index:
            QtWidgets.QMessageBox.warning(
                None, "Invalid Selection", 
                "Please select different components from each image (one magnitude and one phase)"
            )
            return
            
        # Get slider values (0-100)
        weight1 = self.ui.image1_component1_slider.value() / 100.0
        weight2 = self.ui.image2_component1_slider.value() / 100.0
        
        # Get dimensions from the first image
        height, width = self.original_images[0].shape[:2]
        
        # Check if images have different dimensions
        if self.magnitudes[0].shape != self.magnitudes[1].shape:
            # Resize second image components to match first image
            self.magnitudes[1] = cv2.resize(self.magnitudes[1], 
                                          (self.magnitudes[0].shape[1], self.magnitudes[0].shape[0]))
            self.phases[1] = cv2.resize(self.phases[1], 
                                      (self.phases[0].shape[1], self.phases[0].shape[0]))
        
        # Create empty DFT component
        mixed_dft = np.zeros((height, width, 2), dtype=np.float32)
        
        # Apply weights to appropriate components
        if comp1_index == 0:  # Image 1 has magnitude
            # Create polar form with weighted magnitude and phase from image 2
            magnitude = np.exp(self.magnitudes[0]/20) * weight1 + np.exp(self.magnitudes[1]/20) * (1-weight1)
            phase = self.phases[1] * weight2 + self.phases[0] * (1-weight2)
        else:  # Image 1 has phase
            # Create polar form with weighted magnitude from image 2 and phase from image 1
            magnitude = np.exp(self.magnitudes[1]/20) * weight2 + np.exp(self.magnitudes[0]/20) * (1-weight2)
            phase = self.phases[0] * weight1 + self.phases[1] * (1-weight1)
        
        # Convert polar to cartesian
        mixed_dft[:,:,0] = magnitude * np.cos(phase)
        mixed_dft[:,:,1] = magnitude * np.sin(phase)
        
        # Inverse shift
        inverse_shift = np.fft.ifftshift(mixed_dft)
        
        # Inverse DFT
        reconstructed = cv2.idft(inverse_shift)
        reconstructed = cv2.magnitude(reconstructed[:,:,0], reconstructed[:,:,1])
        
        # Normalize reconstructed image
        reconstructed_normalized = cv2.normalize(reconstructed, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        # Create output window if not already created
        if self.output_window is None:
            from UI_Output import Ui_Output
            self.output_window = QtWidgets.QMainWindow()
            self.output_ui = Ui_Output(self.output_window)
            self.output_ui.setupUi(self.output_window)
            self.output_ui.appManager = self  # Set reference to this class for abort method
        
        # Update output window progress bar
        self.output_ui.progressBar.setValue(100)
        
        # Display result in output window
        self.output_ui.groupBox_image1_5.setTitle("Mixed DFT Components")
        self.output_ui.output_1.setImage(np.transpose(reconstructed_normalized, (1, 0)))
        self.output_window.show()
    
    def load_harris_image(self):
        """Load image for Harris corner detection"""
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Open Image for Harris Detection", "", 
            "Images (*.png *.jpg *.jpeg *.bmp *.tif);;All Files (*)"
        )
        
        if file_path:
            # Read image in color
            self.harris_image = cv2.imread(file_path)
            if self.harris_image is None:
                QtWidgets.QMessageBox.warning(None, "Error", "Could not open image!")
                return
            
            # Convert BGR to RGB for display
            rgb_image = cv2.cvtColor(self.harris_image, cv2.COLOR_BGR2RGB)
            transpose_image = np.transpose(rgb_image, (1, 0, 2))
            # Display in original image view
            self.ui.harris_original_image.setImage(transpose_image)
            
            # Clear other views
            self.ui.harris_builtin_image.clear()
            self.ui.harris_manual_image.clear()
    
    def detect_harris_corners(self):
        """Detect corners using Harris corner detection"""
        if self.harris_image is None:
            QtWidgets.QMessageBox.warning(None, "Error", "Please load an image first!")
            return
        
        # Get k-value from slider
        k = self.ui.k_slider.value() / 1000.0
        
        # Convert to grayscale
        gray = cv2.cvtColor(self.harris_image, cv2.COLOR_BGR2GRAY)
        
        # BUILT-IN HARRIS IMPLEMENTATION
        # Convert to float32
        gray_float = np.float32(gray)
        
        # Apply cornerHarris function
        dst = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=k)
        
        # Dilate result for marking corners
        dst = cv2.dilate(dst, None)
        
        # Create color image copy for marking corners
        harris_builtin = cv2.cvtColor(self.harris_image.copy(), cv2.COLOR_BGR2RGB)
        
        # Find coordinates of corner points
        corner_threshold = 0.01 * dst.max()
        y_coords, x_coords = np.where(dst > corner_threshold)
        
        # Draw circles at corner points (red)
        for y, x in zip(y_coords, x_coords):
            cv2.circle(harris_builtin, (x, y), radius=3, color=(255, 0, 0), thickness=-1)
        
        # Display built-in result
        transpose_image = np.transpose(harris_builtin, (1, 0, 2))
        self.ui.harris_builtin_image.setImage(transpose_image)
        
        # MANUAL HARRIS IMPLEMENTATION
        # Step 1: Calculate derivatives
        Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        
        # Step 2: Calculate products of derivatives
        Ixx = np.square(Ix)
        Iyy = np.square(Iy)
        Ixy = Ix * Iy
        
        # Step 3: Apply Gaussian blur to get sum of products in the neighborhood
        Sxx = cv2.GaussianBlur(Ixx, (3,3), 0)
        Syy = cv2.GaussianBlur(Iyy, (3,3), 0)
        Sxy = cv2.GaussianBlur(Ixy, (3,3), 0)
        
        # Step 4: Calculate Harris response function
        # R = det(M) - k * trace(M)^2
        det_M = (Sxx * Syy) - (Sxy ** 2)
        trace_M = Sxx + Syy
        R = det_M - k * (trace_M ** 2)
        
        # Create color image copy for marking corners
        harris_manual = cv2.cvtColor(self.harris_image.copy(), cv2.COLOR_BGR2RGB)
        
        # CHANGE: Draw circles instead of coloring individual pixels
        # Find coordinates of corner points
        manual_threshold = 0.01 * R.max()
        y_coords, x_coords = np.where(R > manual_threshold)
        
        # Draw circles at corner points (blue)
        for y, x in zip(y_coords, x_coords):
            cv2.circle(harris_manual, (x, y), radius=3, color=(0, 0, 255), thickness=-1)
        
        # Display manual result
        transpose_image = np.transpose(harris_manual, (1, 0, 2))
        self.ui.harris_manual_image.setImage(transpose_image)
    
    def abort(self):
        """Handle abortion of image processing operations"""
        print("Processing aborted by user")
        # Add any cleanup code here if needed