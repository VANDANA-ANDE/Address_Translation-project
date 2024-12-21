# simulation.py

def split_virtual_address(virtual_address, page_size):
    """
    Splits the virtual address into a page number and an offset.
    """
    page_number = virtual_address // page_size
    offset = virtual_address % page_size
    return page_number, offset

def simulate_address_translation(virtual_address, page_size, tlb, page_table):
    """
    Simulates the entire address translation process.
    """
    # Step 1: Split Virtual Address into Page Number and Offset
    page_number, offset = split_virtual_address(virtual_address, page_size)

    # Step 2: Check TLB for Page Number
    physical_frame = tlb.get(page_number)
    if physical_frame is not None:
        # TLB Hit
        access_time = 10  # Example time for a TLB hit
        return physical_frame * page_size + offset, "TLB Hit", access_time

    # Step 3: Check 1-Level Page Table for Page Number
    physical_frame = page_table.get(page_number, -1)
    if physical_frame != -1:
        # Page Table Hit
        tlb[page_number] = physical_frame  # Add to TLB
        access_time = 100  # Example time for a page table hit
        return physical_frame * page_size + offset, "Page Table Hit", access_time

    # Step 4: Page Fault
    access_time = 1000  # Example time for handling a page fault
    return -1, "Page Fault", access_time
