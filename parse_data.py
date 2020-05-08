from single_point import parse


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """

    final_x_matrix = list()
    final_y_vector = list()

    f = open(data_file_full_path)
    for line in f:
        ans = parse(line.split(", "))
        final_x_matrix.append(ans[0])
        final_y_vector.append(ans[1])
    f.close()
    return final_x_matrix, final_y_vector


