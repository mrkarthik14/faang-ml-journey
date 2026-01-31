# 📘 Week 01 — Linear Algebra Foundations for Machine Learning

## 🎯 Objective

Build **deep intuition** and **from-scratch implementations** of core linear algebra concepts that power Machine Learning algorithms.

This week focuses on:

- Understanding vectors and matrices **geometrically and algebraically**
- Implementing operations **without NumPy shortcuts**
- Connecting math directly to **real ML use cases**

---

## 🧠 Concepts Covered

### 🔹 Vectors

- Vector representation
- Vector addition & subtraction
- Scalar multiplication
- Vector magnitude (L2 norm)
- Geometric interpretation

### 🔹 Dot Product

- Algebraic definition
- Geometric intuition (similarity, projection)
- Why dot product appears everywhere in ML

### 🔹 Matrices

- Matrix as a linear transformation
- Matrix–vector multiplication
- Matrix–matrix multiplication
- Identity matrix (conceptual)
- Why data is represented as matrices in ML

---

## 🛠️ Implementations (From Scratch)

All implementations are written **without using NumPy linear algebra utilities** to ensure true understanding.

### 📂 `code/`

| File                       | Description                                       |
| -------------------------- | ------------------------------------------------- |
| `vector_operations.py`     | Vector addition, scalar multiplication, magnitude |
| `dot_product.py`           | Manual dot product implementation + tests         |
| `matrix_multiplication.py` | Matrix–vector & matrix–matrix multiplication      |
| `vector_library.py`        | Mini vector class (`add`, `dot`, `norm`, etc.)    |

✅ All results are **verified against NumPy** for correctness.

---

## 📊 Applied Work

### 📓 `notebooks/`

**California Housing EDA**

- Dataset loaded and explored
- Manual correlation calculations
- Data interpreted as matrices
- Visualizations using `matplotlib`

---

## 🧪 Key Experiments

- Compared **manual implementations vs NumPy**
- Visualized matrix transformations
- Explained dot product as a **similarity measure**
- Demonstrated how linear algebra enables:
  - Linear regression
  - Gradient descent
  - Feature interactions

---

## 📚 Learning Resources Used

- 🎓 Andrew Ng — ML Foundations & Linear Algebra Review
- 📘 _Hands-On Machine Learning_ — Chapters 1–2
- 🎥 3Blue1Brown — _Essence of Linear Algebra_

---

## 🧾 Deliverables Checklist

- [x] Vector operations implemented from scratch
- [x] Dot product implemented & explained intuitively
- [x] Matrix multiplication coded manually
- [x] NumPy verification completed
- [x] California Housing EDA notebook
- [x] Notes & reflections documented

---

## 🎯 Key Takeaways

- Linear algebra is **not abstract math** — it’s how ML _thinks_
- Dot product = similarity → core of prediction
- Matrices = transformations → core of learning
- Implementing from scratch removes **black-box thinking**

---

➡️ **Next:** _Week 02 — Statistics & Linear Regression_
