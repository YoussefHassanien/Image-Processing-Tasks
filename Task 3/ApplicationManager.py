from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt
import logging, time
from ImageClass import *


# Standard Logging Levels:

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename="results.log", level=logging.INFO, format='%(asctime)s - %(message)s')

class WorkerThread(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        # Perform your time-consuming operation here
        for i in range(1, 6):
            self.msleep(2000)  # Simulating a time-consuming operation
            if self.isInterruptionRequested():
                print("Thread interrupted. Aborted.")
                return

            print(f"Task {i} completed")
        self.finished_signal.emit()

class AppManager:
    def __init__(self, ui):
        self.UI = ui
        self.RawImageViews = [ui.Image_1, ui.Image_2]
        self.ComponentImageViews = [ui.Image1_component, ui.Image2_component]
        self.Images = {
            0: None,
            1: None,
        }
        # The list below is not list of image views, but rather 1.components displayed, 2.slider_value, 3.index of combobox
        self.ComponentImages = [[None, 0, 0], [None, 0, 0], [None, 0, 0], [None, 0, 0]]
        self.reconstructed_image_uint8 = None
        self.timer = None
        self.start_time = None
        self.end_time = None
        self.first_press_x_coordinates = 0
        self.first_press_y_coordinates = 0
        self.mixing_type_comboBox_previous_index = 0
        self.components_comboBoxes = [self.UI.Image1_component_comboBox, self.UI.Image2_component_comboBox]

    def load_image(self, image_view):
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
            file_path, _ = file_dialog.getOpenFileName()

            if file_path:
                image_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(image_array, (200, 200))

                image_object = OurImage(resized_image)
                self.Images[int(image_view.objectName()[-1]) - 1] = image_object
                self.display_image(image_view, resized_image)
                self.view_component(int(image_view.objectName()[-1]) - 1, 0)

    @staticmethod
    def display_image(image_view, image_array):
            transposed_array = np.transpose(image_array)
            image_view.clear()
            image_view.setImage(transposed_array)

    def view_component(self, image_view_index, component_index):
        if self.Images[image_view_index]:
            if component_index == 0:
                self.display_image(self.ComponentImageViews[image_view_index],
                                   self.Images[image_view_index].viewed_magnitude)
            else:
                self.display_image(self.ComponentImageViews[image_view_index],
                                   self.Images[image_view_index].Components[component_index])
            self.ComponentImages[image_view_index][0] = self.Images[image_view_index].Components[component_index]
            self.ComponentImages[image_view_index][2] = component_index
            index_to_component = ["Magnitude", "Phase", "Real Part", "Imaginary Part"]
            logging.info(f"Image View {image_view_index + 1} switched to component {index_to_component[component_index]}.")

    def update_slider_values(self):
        sliders = [self.UI.image1_component1_slider, self.UI.image2_component1_slider]
        for i in range(2):
            self.ComponentImages[i][1] = sliders[i].value()

    def run_function(self):
        # Create and start the worker thread
        self.worker_thread = WorkerThread()
        self.worker_thread.finished_signal.connect(self.function_finished)
        self.worker_thread.start()

    @staticmethod
    def function_finished():
        print("Synchronous Function completed")

    def abort(self):
        if hasattr(self, 'worker_thread') and self.worker_thread.isRunning():
            print("Aborting...")
            self.worker_thread.requestInterruption()

    def mix(self):
        self.UI.open_window()
        self.start_progress()
        self.run_function()
        self.start_time = time.time()
        image = self.component_mix()
        self.display_image(self.UI.ui.output_1, image)

    def component_mix(self):
        self.update_slider_values()
        # 1. Magnitude 2. Phase
        output_components = [0, 0]
        for component_value, slider_value, component_type in self.ComponentImages:
            if component_value is None:
                continue
            output_components[component_type] += component_value * slider_value / 100.0

        self.end_time = time.time()
        logging.info(f"Components Mixing Done in {self.end_time - self.start_time} second(s)")
        return self.reconstruct_image(output_components)


    def start_progress(self):
        self.UI.ui.progressBar.setValue(0)
        interval = 40 # milliseconds

        # Create a timer to update the progress
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(interval)

    def update_progress(self):
        # Increment the progress bar value
        current_value = self.UI.ui.progressBar.value()
        new_value = min(current_value + int(100 / (1000 / 40)), 100)
        self.UI.ui.progressBar.setValue(new_value)
        # Stop the timer when the progress reaches 100%
        if new_value == 100:
            self.timer.stop()

    def reconstruct_image(self, output_components):
        output_mag_phase = (output_components[0]) * np.exp(1j * output_components[1])
        output_combined_components = output_mag_phase
        
        # Perform the Inverse Fourier Transform to reconstruct the image
        reconstructed_image = np.fft.ifft2(np.fft.ifftshift(output_combined_components)).real
        # Normalize the pixel values to the range [0, 255] for display
        reconstructed_image_normalized = cv2.normalize(reconstructed_image, None, 0, 255, cv2.NORM_MINMAX)
        # Convert to uint8 for display (grayscale image)
        self.reconstructed_image_uint8 = np.uint8(reconstructed_image_normalized)
        return self.reconstructed_image_uint8




    def hide_components(self):     
        comboboxes_all_components = ["FT Magnitude", "FT Phase"]
        for i in range(2):
            self.components_comboBoxes[i].clear()
            self.components_comboBoxes[i].insertItems(0, comboboxes_all_components)

