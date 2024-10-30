import vtk
from .conversion import conv_to_dataframe


TEST_FILE = "/mnt/c/Users/Jtd52/Documents/VirginiaTech/Research/GTL/tinker_output/revised_viscosity_litho_1763/solution/solution-00011.0000.vtu"
def read_vtu(file_name = TEST_FILE):

    reader = vtk.vtkXMLUnstructuredGridReader()

    reader.SetFileName(file_name)

    reader.Update()
    return conv_to_dataframe(reader.GetOutput())



def read_pvtu(file_name):

    reader = vtk.vtkXMLPUnstructuredGridReader()

    reader.SetFileName(file_name)

    reader.Update()

    return conv_to_dataframe(reader.GetOutput())



