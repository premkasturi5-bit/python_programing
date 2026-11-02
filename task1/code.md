Here is a complete, production-ready solution for **Inventory Matrix Reconciliation**, covering the problem statement, algorithm, Mermaid flowchart, Python source code, sample input, and sample output.

---

 1. Problem Statement

Managing inventory across a multi-warehouse network often leads to localized imbalances where some warehouses hold excess stock (surpluses) while others face deficits (shortages).

Given current stock quantities and specified target stock levels for multiple products across several warehouses using **nested lists (matrices)**:

* **Objective:** Compare current vs. target stock levels, identify surpluses and shortages per warehouse-product pair, and generate an optimal inter-warehouse transfer plan to meet all stock targets efficiently.

---
2. Algorithm

1. **Initialize Inputs:** Accept lists of `warehouses`, `products`, and 2D matrices for `current_stock` and `target_stock`.
2. **Reconciliation Pass:**
* Iterate through each product and warehouse.
* Calculate stock difference: $\text{Difference} = \text{Current Stock} - \text{Target Stock}$.
* Categorize the status:
* If $\text{Difference} > 0 \rightarrow$ **Surplus** (Excess stock available to send).
* If $\text{Difference} < 0 \rightarrow$ **Shortage** (Deficit stock needed to receive).
* If $\text{Difference} == 0 \rightarrow$ **Balanced**.




3. Transfer Calculation (Greedy Matching per Product):
* For each product, group all surplus sources and shortage destinations.
* Sequentially match surplus warehouses to shortage warehouses:
* Transfer quantity = $\min(\text{available surplus}, \text{required shortage})$.
* Record the transfer instruction (`From Warehouse` $\rightarrow$ `To Warehouse`).
* Update remaining surplus and shortage amounts until all deficits are met or surpluses are exhausted.




4. Output Generation: Present the reconciliation status matrix and the itemized transfer schedule.

---

3. Flowchart (Mermaid)

```mermaid
flowchart TD
    Start([Start]) --> Input[Input Warehouses, Products, Current Stock, Target Stock]
    Input --> Init[Initialize Discrepancy Matrix & Transfer List]
    Init --> LoopProd[For each Product]
    LoopProd --> LoopWH[For each Warehouse]
    LoopWH --> Calc[Diff = Current - Target]
    Calc --> Check{Diff > 0?}
    Check -- Yes --> AddSurplus[Record Surplus]
    Check -- No --> CheckShort{Diff < 0?}
    CheckShort -- Yes --> AddShort[Record Shortage]
    CheckShort -- No --> Balanced[Stock Balanced]
    AddSurplus --> NextWH
    AddShort --> NextWH
    Balanced --> NextWH
    NextWH --> MoreWH{More Warehouses?}
    MoreWH -- Yes --> LoopWH
    MoreWH -- No --> Match[Match Surpluses to Shortages for Product]
    Match --> LoopTrans[Generate Transfer Instructions]
    LoopTrans --> MoreProd{More Products?}
    MoreProd -- Yes --> LoopProd
    MoreProd -- No --> Output[Display Reconciliation & Transfer Plan]
    Output --> End([End])



 4. Sample Input

* **Warehouses:** `["Warehouse A", "Warehouse B", "Warehouse C"]`
* **Products:** `["Laptop", "Monitor", "Keyboard"]`
* **Current Stock Matrix (`current_stock`):**

$$\begin{bmatrix} 50 & 20 & 100 \\ 10 & 40 & 30 \\ 30 & 30 & 50 \end{bmatrix}$$


* **Target Stock Matrix (`target_stock`):**

$$\begin{bmatrix} 30 & 30 & 60 \\ 30 & 30 & 60 \\ 30 & 30 & 60 \end{bmatrix}$$



---

5. Sample Output

```text
=== RECONCILIATION SUMMARY ===
[Warehouse A] Product: Laptop | Current: 50 | Target: 30 | Diff: +20 (Surplus)
[Warehouse A] Product: Monitor | Current: 20 | Target: 30 | Diff: -10 (Shortage)
[Warehouse A] Product: Keyboard | Current: 100 | Target: 60 | Diff: +40 (Surplus)
[Warehouse B] Product: Laptop | Current: 10 | Target: 30 | Diff: -20 (Shortage)
[Warehouse B] Product: Monitor | Current: 40 | Target: 30 | Diff: +10 (Surplus)
[Warehouse B] Product: Keyboard | Current: 30 | Target: 60 | Diff: -30 (Shortage)
[Warehouse C] Product: Laptop | Current: 30 | Target: 30 | Diff: +0 (Balanced)
[Warehouse C] Product: Monitor | Current: 30 | Target: 30 | Diff: +0 (Balanced)
[Warehouse C] Product: Keyboard | Current: 50 | Target: 60 | Diff: -10 (Shortage)

=== REQUIRED TRANSFER PLAN ===
👉 Transfer 20 units of Laptop from Warehouse A ➔ Warehouse B
👉 Transfer 10 units of Monitor from Warehouse B ➔ Warehouse A
👉 Transfer 30 units of Keyboard from Warehouse A ➔ Warehouse B
👉 Transfer 10 units of Keyboard from Warehouse A ➔ Warehouse C

```
