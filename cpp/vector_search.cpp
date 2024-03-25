// Vector Search functions and algorithms

// Function to find the index of the nearest value to a user-defined value in a (sorted) vector of floats
// Inspired from https://alexsm.com/cpp-closest-lower-bound/

float find_nearest(const std::vector<float>& sorted_vector, float desired_value) {
    // Getting the index of the element which has a value >= input_value
    auto id_nearest = std::lower_bound(sorted_vector.begin(), sorted_vector.end(), desired_value);

    // If nearest value is at the beginning of the vector, function returns the index of the first element
    if (id_nearest == sorted_vector.begin()) {
        return 0;
    }

    // If nearest value is at the end of the vector, function returns the index of the last element
    if (id_nearest == sorted_vector.end()) {
        int vector_size = sorted_vector.size();
        return (vector_size - 1);
    }

    // If desired value is between 2 vector values, function returns the index of the closest element
    float id_lower = *(id_nearest - 1);
    float id_upper = *(id_nearest);
    if (fabs(desired_value - id_lower) < fabs(desired_value - id_upper)) {
        return id_nearest - sorted_vector.begin() - 1;
    }

    // Else, function returns the index of the corresponding element
    return id_nearest - sorted_vector.begin();
}
