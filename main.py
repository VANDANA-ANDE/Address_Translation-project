from simulation import simulate_address_translation

def main():
    # Example configurations
    page_size = 4096
    tlb = {}  # Simulated TLB
    page_table = {0: 5, 1: 7, 2: 3}  # Example page table

    # Get user input
    virtual_address = int(input("Enter Virtual Address: "))
    
    # Simulate translation
    physical_address, status, access_time = simulate_address_translation(
        virtual_address, page_size, tlb, page_table
    )

    # Print results
    if physical_address != -1:
        print(f"Physical Address: {physical_address} | Status: {status} | Access Time: {access_time}ns")
    else:
        print(f"Status: {status} | Page Fault | Access Time: {access_time}ns")

if __name__ == "__main__":
    main()
