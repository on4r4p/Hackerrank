def amount_earned():
        total_amount = 0
        for i in range(customers):
                size, price = list(map(int, input().split()))

                if size in sizes:
                        total_amount += price
                        sizes.remove(size)

        return total_amount

amounts = int(input())
sizes = list(map(int, input().split()))
customers = int(input())
total_amount = amount_earned()
print(total_amount)
