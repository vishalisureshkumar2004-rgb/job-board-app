# I'm H1 tag
## I'm H2
### I'm H3

- This is for bullet points
- this is another bullet point
- this is ordered list

1. This is numbered list
2. This is another number

```txt
This is used for code blocks
```

```sh
sudo apt update
```

```py
import numpy
import pandas

def hello():
  print("Hello")
```

Hi `how` are you **this** is for an example.

---

Here's a random but practical Python example that analyzes a list of student scores.

## Python Code

```python
def analyze_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    return {
        "Highest": highest,
        "Lowest": lowest,
        "Average": round(average, 2)
    }


student_scores = [78, 92, 85, 67, 90, 88]

result = analyze_scores(student_scores)

for key, value in result.items():
    print(f"{key}: {value}")
```

### Sample Output

```text
Highest: 92
Lowest: 67
Average: 83.33
```

---

# Explanation

### 1. Function Definition

```python
def analyze_scores(scores):
```

Creates a function named `analyze_scores` that accepts a list of numbers.

---

### 2. Find Highest Score

```python
highest = max(scores)
```

Uses Python's built-in `max()` function to find the largest value.

---

### 3. Find Lowest Score

```python
lowest = min(scores)
```

Uses `min()` to determine the smallest value.

---

### 4. Calculate Average

```python
average = sum(scores) / len(scores)
```

* `sum(scores)` adds all numbers.
* `len(scores)` counts how many scores there are.
* Dividing gives the average.

---

### 5. Return Results

```python
return {
    "Highest": highest,
    "Lowest": lowest,
    "Average": round(average, 2)
}
```

Returns a dictionary containing the calculated statistics. `round(..., 2)` limits the average to two decimal places.

---

### 6. Input Data

```python
student_scores = [78, 92, 85, 67, 90, 88]
```

Creates a list of student scores.

---

### 7. Call the Function

```python
result = analyze_scores(student_scores)
```

Runs the function and stores the returned dictionary.

---

### 8. Display Results

```python
for key, value in result.items():
    print(f"{key}: {value}")
```

Loops through each key-value pair in the dictionary and prints it.

---

# Mermaid Flow Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Create list of student scores]
    B --> C[Call analyze_scores(scores)]
    C --> D[Find highest score using max()]
    D --> E[Find lowest score using min()]
    E --> F[Calculate average using sum()/len()]
    F --> G[Create dictionary with results]
    G --> H[Return dictionary]
    H --> I[Loop through dictionary]
    I --> J[Print each result]
    J --> K([End])
```

---

# Execution Flow

```text
Start
   │
   ▼
Student Scores
   │
   ▼
Analyze Function
   │
   ├──► Highest = max()
   ├──► Lowest = min()
   └──► Average = sum()/len()
   │
   ▼
Return Dictionary
   │
   ▼
Print Results
   │
   ▼
End
```

This example demonstrates several core Python concepts in a compact program:

* Defining and calling functions
* Working with lists
* Using built-in functions (`max`, `min`, `sum`, `len`)
* Returning dictionaries
* Iterating over dictionary items with a `for` loop
* Formatting output using f-strings

