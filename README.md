
🔄 Swap Elements in a List (Python)

This simple Python script demonstrates how to **swap two elements in a list** by their positions using tuple unpacking and indexing.

---

📋 Description

The script initializes a list of integers and swaps the elements at two specified positions. Specifically, it swaps the values at **index 3** and **index 6** of the list.


✅ Initial List:

```python
[10, 20, 30, 40, 50, 60, 70]
```

🔁 Swapping Positions:

* `pos1 = 3` → Value: `40`
* `pos2 = 6` → Value: `70`

After swapping:

```python
[10, 20, 30, 70, 50, 60, 40]
```

---

🧠 How It Works

```python
mylist = [10, 20, 30, 40, 50, 60, 70]
pos1, pos2 = 3, 6
get = (mylist[pos1], mylist[pos2])  # Store original values
mylist[pos2], mylist[pos1] = get    # Swap values using tuple unpacking
print(mylist)
```

* **Tuple unpacking** is used to swap values without needing a temporary variable.
* `get` holds the original values to be swapped.
* Values are reassigned to their new positions.

---

▶️ How to Run

1. Save the script in a `.py` file, e.g., `swap_list.py`.
2. Run the script using Python:

```bash
python swap_list.py
```

---

🧪 Output

```
[10, 20, 30, 70, 50, 60, 40]
```

---

📚 Requirements

* Python 3.x

No external libraries are required.

---

📌 Notes

* Indexing starts at `0` in Python.
* Attempting to access invalid indices (e.g., beyond the list length) will raise an `IndexError`.

