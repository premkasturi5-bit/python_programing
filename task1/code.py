def reconcile_inventory(warehouses, products, current_stock, target_stock):
    """
    Reconciles inventory across warehouses and calculates required transfers.
    """
    num_warehouses = len(warehouses)
    num_products = len(products)
    
    reconciliation_results = []
    transfer_plan = []
    for j in range(num_products):
        product_name = products[j]
        surpluses = []
        shortages = []
        
        for i in range(num_warehouses):
            wh_name = warehouses[i]
            curr = current_stock[i][j]
            targ = target_stock[i][j]
            diff = curr - targ
            
            status = "Balanced"
            if diff > 0:
                status = "Surplus"
                surpluses.append({"warehouse": wh_name, "amount": diff})
            elif diff < 0:
                status = "Shortage"
                shortages.append({"warehouse": wh_name, "amount": abs(diff)})
                
            reconciliation_results.append({
                "warehouse": wh_name,
                "product": product_name,
                "current": curr,
                "target": targ,
                "difference": diff,
                "status": status
            })
          
        active_surpluses = [s.copy() for s in surpluses]
        active_shortages = [sh.copy() for sh in shortages]
        
        s_idx, sh_idx = 0, 0
        while s_idx < len(active_surpluses) and sh_idx < len(active_shortages):
            surplus_item = active_surpluses[s_idx]
            shortage_item = active_shortages[sh_idx]
            
            transfer_qty = min(surplus_item["amount"], shortage_item["amount"])
            
            if transfer_qty > 0:
                transfer_plan.append({
                    "product": product_name,
                    "from_warehouse": surplus_item["warehouse"],
                    "to_warehouse": shortage_item["warehouse"],
                    "quantity": transfer_qty
                })
                
            surplus_item["amount"] -= transfer_qty
            shortage_item["amount"] -= transfer_qty
            
            if surplus_item["amount"] == 0:
                s_idx += 1
            if shortage_item["amount"] == 0:
                sh_idx += 1
                
    return reconciliation_results, transfer_plan


if __name__ == "__main__":
    warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]
    products = ["Laptop", "Monitor", "Keyboard"]
    
   
    current_stock = [
        [50, 20, 100], 
        [10, 40, 30],  
        [30, 30, 50]   
    ]
    
    target_stock = [
        [30, 30, 60],  
        [30, 30, 60],  
        [30, 30, 60]  
    ]
    
    results, transfers = reconcile_inventory(warehouses, products, current_stock, target_stock)
    
    print("=== RECONCILIATION SUMMARY ===")
    for r in results:
        print(f"[{r['warehouse']}] Product: {r['product']} | Current: {r['current']} | Target: {r['target']} | Diff: {r['difference']:+d} ({r['status']})")
        
    print("\n=== REQUIRED TRANSFER PLAN ===")
    if not transfers:
        print("No transfers needed. All warehouses meet target stock.")
    for t in transfers:
        print(f"👉 Transfer {t['quantity']} units of {t['product']} from {t['from_warehouse']} ➔ {t['to_warehouse']}")
