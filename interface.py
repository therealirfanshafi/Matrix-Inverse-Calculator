# this is the main program, it provides a GUI for the matrix

#import of modules
import tkinter as tk
from tkinter import messagebox
from matrix_calculator import inverse

# creating the main window
root = tk.Tk()
root.title("Matrix Inverse Calculator")
root.geometry("800x600")
root.configure(bg="#0e0f0f")

def display_inverse():  # module to display the inverse of the matrix

    try:
        matrix = list(map(lambda x: list(map(lambda y: int(y.get()) if float(y.get()) // 1 == float(y.get()) else float(y.get()), x)), matrix_entry_fields))  # a single line of code which gets the value entered in each input field, and then converts it to a float or int depending on its type
    except ValueError or TypeError:  # if invalid inputs are given an error message is shown
        messagebox.showerror("Invalid Matrix", "Matrix elements must be numerical and all the elements should be present")
        return
    
    try:
        inverse_matrix = inverse(matrix)
    except ValueError:  # if its a singular matrix, an error message is shown
        messagebox.showerror("Inverse does not exist", "Matrix is singular")
        return
    
    # creates and formats a new window
    inverse_matrix_window = tk.Tk()
    inverse_matrix_window.configure(bg = "#0e0f0f")
    inverse_matrix_frame = tk.Frame(inverse_matrix_window, bg = "#0e0f0f")  # a frame for the matrix part of the inverse matrix

    for i in range(len(inverse_matrix[1])):  # arranges the matrix elements in order of the rows and columns using the grid system
        for j in range(len(inverse_matrix[1])):
            tk.Label(inverse_matrix_frame, text=str(inverse_matrix[1][i][j]), bg = "#0e0f0f", fg = "#FFFFFF").grid(row=i+1, column=j+1, padx= 5, pady= 5)
    
    # sets the brackets around the matrix
    tk.Label(inverse_matrix_frame, text="[", font=("Courier New", len(inverse_matrix[1])*40), bg = "#0e0f0f", fg = "#FFFFFF").grid(row=0, column=0, rowspan=len(inverse_matrix[1]) + 2)
    tk.Label(inverse_matrix_frame, text="]", font=("Courier New", len(inverse_matrix[1])*40), bg = "#0e0f0f", fg = "#FFFFFF").grid(row=0, column=len(inverse_matrix[1]) + 2, rowspan=len(inverse_matrix[1]) + 2)
    inverse_matrix_frame.grid(row=0, column=1, rowspan=len(inverse_matrix[1]) + 2)

    determinant_frame = tk.Frame(inverse_matrix_window, bg = "#0e0f0f")  # frame fror the determinant part of the inverse matrix
    determinant_frame.grid(row= (len(inverse_matrix[1]) + 2) // 2, column = 0)
    # creates 3 labels making it look like 1/determinant
    tk.Label(determinant_frame, text = "1", bg = "#0e0f0f", fg = "#FFFFFF").grid(row = 0, column=0)
    tk.Label(determinant_frame, text = "____", bg = "#0e0f0f", fg = "#FFFFFF").grid(row = 1 , column=0)
    tk.Label(determinant_frame, text = str(inverse_matrix[0]), bg = "#0e0f0f", fg = "#FFFFFF").grid(row = 2, column=0)
    

def create_matrix():  # module to display an entry field for the matrix

    try:
        matrix_dimension = int(size_entry_field.get())  # gets the dimensions of the matrix
    except:  # error message for invalid argument
        messagebox.showerror("Invalid Size", "You must enter a single integer as the size")
        size_entry_field.delete(0, tk.END)
        return

    if matrix_dimension <= 1:
        messagebox.showerror("Invalid Size", "Size must be at least 2")
        size_entry_field.delete(0, tk.END)
        return

    global matrix_frame
    global matrix_entry_fields

    if matrix_frame:  # removes the matrix on the screen if it already exists
        matrix_frame.forget()
    matrix_frame = tk.Frame(root, bg= "#0e0f0f")  # frame to display the matrix
    matrix_frame.pack()

    matrix_entry_fields = []  # contains each of the input boxes for each element of the matrix
    for i in range(matrix_dimension):  # uses the grid system to position each input box in its correct coressponding location
        matrix_entry_fields.append([])
        for j in range(matrix_dimension):
            field = tk.Entry(matrix_frame, width=5, bg="#000000", fg="#FFFFFF", insertbackground="#FFFFFF")
            field.grid(row = i + 1, column= j + 1, padx=5, pady=5)
            matrix_entry_fields[-1].append(field)

    # draws the matrix brackets
    tk.Label(matrix_frame, text="[", font=("Courier New", matrix_dimension*40), bg= "#0e0f0f", fg = "#FFFFFF").grid(row=0, column=0, rowspan=matrix_dimension + 2)
    tk.Label(matrix_frame, text="]", font=("Courier New", matrix_dimension*40), bg= "#0e0f0f", fg = "#FFFFFF").grid(row=0, column=matrix_dimension + 2, rowspan=matrix_dimension + 2)

    get_inverse = tk.Button(matrix_frame, text="Show inverse", command=display_inverse, bg= "#000000", fg = "#FFFFFF")  # button to display the inverse, calls the display_inverse() module above if pressed
    get_inverse.grid(row=matrix_dimension + 3, column=0, columnspan=matrix_dimension + 2)


if __name__ == "__main__":  # main program starts here
    # a frame to input the dimensions of the matrix
    size_frame = tk.Frame(root, bg = "#0e0f0f")
    size_frame.pack(pady=(10, 20))
    matrix_frame = None
    
    # labels, input boxes and button
    size_label = tk.Label(size_frame, text= "Enter the dimension of the matrix here", font=("Arial", 12), bg ="#0e0f0f", fg = "#FFFFFF")
    size_entry_field = tk.Entry(size_frame, width= 5, bg ="#000000", fg = "#FFFFFF", insertbackground="#FFFFFF")
    confirm_size = tk.Button(size_frame, text="Create Matrix", font=("Arial", 12), command=create_matrix, bg ="#000000", fg = "#FFFFFF")  # pressing button calls the create_matrix() module above

    size_label.grid(row= 0, column= 0, padx=10)
    size_entry_field.grid(row=0, column=1)
    confirm_size.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()