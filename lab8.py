import random
import time

class Cafe:
    def __init__(self, num_tables=10, num_waiters=3, capacity_margin=0.5, order_processing_time=5):
        self.num_tables = num_tables
        self.num_waiters = num_waiters
        self.tables = [0] * num_tables  # Initialize all tables as empty
        self.waiters = [{'position': 'corridor', 'customer_order': None, 'timer': 0, 'table': None} for _ in range(num_waiters)]
        self.customers = []
        self.profit = 0
        self.capacity_margin = capacity_margin
        self.kitchen = {'pending_orders': [], 'ready_orders': []}
        self.order_processing_time = order_processing_time
        self.hour = 10

    def assign_table(self, customer):
        empty_tables = [i for i, table in enumerate(self.tables) if table == 0]
        if empty_tables:
            table_idx = random.choice(empty_tables)
            self.tables[table_idx] = customer
            customer['table'] = table_idx
            return True
        else:
            return False

    def check_capacity(self):
        return len(self.customers) < self.num_tables * (1 + self.capacity_margin)

    def take_order(self, customer):
        available_dishes = ["Pizza", "Burger", "Pasta", "Salad"]
        num_dishes = random.choice([1, 2, 4])
        order = random.sample(available_dishes, num_dishes)
        customer['order'] = order
        print(f"Customer at table {customer['table']} ordered: {', '.join(order)}")
        self.kitchen['pending_orders'].append((customer['table'], order, random.randint(5, 10)))
        customer['wait_time'] = 0
        # Additional: Waiter takes the order to the kitchen
        waiter = random.choice(self.waiters)
        if waiter['position'] == 'corridor':
            waiter['customer_order'] = order
            waiter['position'] = 'kitchen'
            waiter['table'] = customer['table']
            print(f"Waiter {self.waiters.index(waiter)} took the order to the kitchen for table {customer['table']}")

    def serve_meal(self, waiter):
        if waiter['position'] == 'kitchen' and waiter['customer_order']:
            dish = waiter['customer_order'][0]
            waiter['customer_order'].pop(0)
            waiter['position'] = 'table'
            table = waiter['table']
            print(f"Waiter {self.waiters.index(waiter)} served {dish} to table {table}")

    def check_customer_wait_time(self, customer):
        if customer['wait_time'] >= 2:
            print(f"Customer at table {customer['table']} ran out of time and left the table.")
            self.tables[customer['table']] = 0
            self.customers.remove(customer)

    def calculate_profit(self):
        profit = random.uniform(5, 15)
        self.profit += profit
        return profit

    def process_pending_orders(self):
        for order_info in self.kitchen['pending_orders']:
            table, order, preparation_time = order_info
            if table is not None:
                if preparation_time <= 0:
                    self.kitchen['pending_orders'].remove(order_info)
                    self.serve_dish(table, order)
                else:
                    preparation_time -= 1

    def serve_dish(self, table, dish):
        for customer in self.customers:
            if customer['table'] == table:
                customer['order'].remove(dish)
                if not customer['order']:
                    self.profit += random.uniform(5, 15)
                    self.tables[customer['table']] = 0
                    self.customers.remove(customer)
                break

    def simulate(self):
        for hour in range(self.hour, 22):
            self.hour = hour
            print(f"=== Hour {hour}:00 ===")

            if self.check_capacity():
                # Customers arrive
                if hour == 20:
                    num_customers = random.randint(3, 7)
                else:
                    num_customers = random.randint(1, 3)

                for _ in range(num_customers):
                    customer = {'table': None, 'order': [], 'wait_time': 0}
                    if self.assign_table(customer):
                        self.customers.append(customer)
                        print(f"Customer arrived at table {customer['table']}")
                        self.take_order(customer)
                        # Additional: Serve the order
                        self.serve_meal(random.choice(self.waiters))
            
            # Check customer wait times
            for customer in self.customers:
                customer['wait_time'] += 1
                self.check_customer_wait_time(customer)

            # Process pending orders
            self.process_pending_orders()

            # Check and handle orders in the kitchen
            if self.kitchen['ready_orders']:
                for waiter, dish in self.kitchen['ready_orders']:
                    if waiter['position'] == 'kitchen':
                        waiter['customer_order'] = [dish]
                        waiter['position'] = 'table'
                        table = waiter['table']
                        print(f"Waiter {self.waiters.index(waiter)} served a dish to table {table}")
                        self.tables[table] = waiter
                        self.kitchen['ready_orders'].remove((waiter, dish))
            
            time.sleep(1)

        print("=== Closing Time ===")
        self.profit += sum([self.calculate_profit() for customer in self.customers if len(self.customers) > 0])
        print(f"Total profit: ${self.profit:.2f}")

def main():
    num_tables = int(input("Enter the number of tables: "))
    num_waiters = int(input("Enter the number of waiters: "))
    capacity_margin = float(input("Enter the capacity margin (e.g., 0.5 for 50%): "))
    
    cafe = Cafe(num_tables, num_waiters, capacity_margin)
    cafe.simulate()

if __name__ == '__main__':
    main()