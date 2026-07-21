from flask import Flask, render_template, request

app = Flask(__name__)


def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    steps = []

    while low <= high and x >= arr[low] and x <= arr[high]:

        if low == high:
            if arr[low] == x:
                steps.append(f"Element found at index {low}")
                return low, steps
            return -1, steps

        # Interpolation formula
        pos = low + ((x - arr[low]) * (high - low) //
                     (arr[high] - arr[low]))

        steps.append(
            f"Checking position {pos}, value = {arr[pos]}"
        )

        if arr[pos] == x:
            steps.append(f"Element found at index {pos}")
            return pos, steps

        if arr[pos] < x:
            low = pos + 1
            steps.append("Searching right side")
        else:
            high = pos - 1
            steps.append("Searching left side")

    steps.append("Element not found")
    return -1, steps


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    steps = []

    if request.method == "POST":

        array = request.form["array"]
        target = int(request.form["target"])

        arr = list(map(int, array.split(",")))

        arr.sort()

        index, steps = interpolation_search(arr, target)

        if index != -1:
            result = f"Element {target} found at index {index}"
        else:
            result = f"Element {target} not found"


    return render_template(
        "index.html",
        result=result,
        steps=steps
    )


if __name__ == "__main__":
    app.run(debug=True)