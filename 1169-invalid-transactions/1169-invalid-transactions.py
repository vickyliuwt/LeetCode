class Solution(object):
    def invalidTransactions(self, transactions):
        person = defaultdict(list)
        n = len(transactions)
        valid = [True] * n
        
        # Step 1: Parse string records and group by person name
        for i, transaction in enumerate(transactions):
            details = transaction.split(',')
            person[details[0]].append([int(details[1]), int(details[2]), details[3], i])

        # Step 2: Validate transactions per individual using sliding windows
        for individual, trades in person.items():
            # Sort chronologically by timestamp
            trades.sort(key=lambda x: x[0])
            window = [] 
            
            for j, (time, amount, location, idx) in enumerate(trades):
                # Condition 1: Amount exceeds $1000
                if amount > 1000:
                    valid[idx] = False
                    
                # Evict entries outside the 60-minute window
                while window and time - trades[window[0]][0] > 60:
                    window.pop(0)
                    
                # Condition 2: City mismatch within 60 minutes
                for wj in window:
                    if trades[wj][2] != location:
                        valid[idx] = False
                        valid[trades[wj][3]] = False
                        
                window.append(j)

        # Reconstruct list of invalid transaction strings
        return [transactions[i] for i in range(n) if not valid[i]]