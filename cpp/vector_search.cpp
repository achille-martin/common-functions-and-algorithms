// MIT License

// Copyright (c) 2023-2024 Achille MARTIN

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

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
