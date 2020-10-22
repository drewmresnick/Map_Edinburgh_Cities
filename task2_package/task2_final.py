#Import pyplot for graphing
import numpy
from matplotlib import pyplot as plt

#allows all functions to be accessed via module
__all__ = ['parse_coords','read_regions', 'plot_regions']

def parse_coords(line):
    '''Function used to read lines of data and create tuples of two floats a,b (this function uses a,b as variable names in the tuple as they are not yet set as coordinates)'''
    line = line[1:-2:] #read all characters between the brackets
    a,b = line.split(', ') #splits the string into the two values a,b at the comma
    return float(a), float(b) #creates a tuple of a,b

def read_regions(Data):
    '''Function used to create a workflow which will loop through an entire dataset and append values and set keys to create dictionaries.
     Each dictionary represents a neighborhood. Function will also skip over bad data'''
    is_coordinates = False #flag is false, will not read line as data
    regions = {} #define dictionary
    with open(Data, 'r') as Data:
        for line in Data.readlines():
            if line.startswith('#'): #reads through lines starting with #
                continue
            elif not is_coordinates and line[0].isalpha(): #if is_coordinates is False and line starts with a letter, will take the line and create a dictionary key
                n_name = line.strip() #N_NAME = NEIGHBOURHOOD NAME (KEY IN DICTIONARY)
                regions[n_name] = []
                is_coordinates = True #function will not begin to read lines as data
            elif line.startswith('('): #for every line that starts with '(' will fun the parse_coords function to convert data
                point = parse_coords(line)
                regions[n_name].append(point) #appending the tuple of a, b into the empty list of the regions dictionary
            elif line.startswith('['): #dealing with bad data
                print(n_name + ' has bad data') #prints to terminal
                is_coordinates = False #does not read lines as data
                continue
            else:
                is_coordinates = False #stops function from reading lines as data
    for region in regions:
        regions[region] = numpy.array(regions[region]) #converting lists to arrays
    plot_regions(regions)


    #use pyplot to enhance map
def plot_regions(regions_dict):
    '''Function to plot dictionaries, will also create formatting for the graph'''
    #call the function outside of the function definition. Creates variable (dictionary) 'regions_dict':
    for region in regions_dict: #plotting all dictionaries that have at least one value
        if regions_dict[region].size >0:
            plt.plot(regions_dict[region][:,0], regions_dict[region][:,1])
    plt.xlabel('Eastings (Meters)')
    plt.ylabel('Northings (Meters)')
    plt.title('Neighborhoods in Edinburgh')
    plt.grid()
    plt.arrow(330000, 660000, 0, 2000, head_width = 1000, color=('black')) #creates a north arrow
    plt.show() #use pyplot to show the plotted data
