# 0x00. Pagination ⚙️➡️ 

This project explores various pagination techniques for a dataset of baby names stored in a CSV file (`Popular_Baby_Names.csv`).  

**Learning Objectives:**

By the end of this project, you should be able to explain, without assistance from search engines:

* How to paginate a dataset using basic page and page_size parameters ( + ).
* How to implement hypermedia pagination for richer client navigation ().
* How to achieve deletion-resilient pagination to handle potential data changes ( + ).

**Requirements:**

* Ubuntu 18.04 LTS
* Python 3.7
* `csv` library
* `typing` module
* `pycodestyle` (version 2.5.*) for code style checks (✅)
* `wc` utility for file length checks ()
* `Popular_Baby_Names.csv` data file ( + )

**Setup:**

1. Download or copy the `Popular_Baby_Names.csv` file to your project directory. (⬇️)

# Tasks
## Task 1. Simple Helper Function (️):
This task involves creating a function named `index_range` that calculates the starting and ending indices for a given page and `page_size`.</br>

### File:
* `0-simple_helper_function.py`: Contains the `index_range` function ().
<br></br>

## Task 2. Simple Pagination ():
Here, you'll implement a server class with a `get_page` method that retrieves specific pages from the baby name dataset based on user-provided page and page_size parameters. The implementation should handle invalid inputs (negative values, non-integers) and potential out-of-range requests ().</br>

### File:
* `1-simple_pagination.py`: Implements the `Server` class with basic pagination (`get_page`) ().
<br></br>

## Task 3. Hypermedia Pagination ():
This task builds upon the previous one by introducing hypermedia pagination. The server's `get_hyper` method should return a dictionary containing additional information about the requested page and its position within the entire dataset, including:

* `page_size`: The number of items in the current page ().
* `page`: The current page number ().
* `data`: The actual page of baby name data ( + ).
* `next_page`: Index of the next page (if available) (➡️).
* `prev_page`: Index of the previous page (if available) (⬅️).
* `total_pages`: The total number of pages in the dataset ().</br>

### File:
* `2-hypermedia_pagination.py`: Extends the server with hypermedia features (`get_hyper`) ().
<br></br>

## Task 4. Deletion-Resilient Hypermedia Pagination ( + ):
This task introduces deletion-resilient pagination. The goal is to ensure that users don't miss entries even if rows are removed from the original dataset between requests. The server achieves this by maintaining an indexed version of the data (`indexed_dataset`) that tracks the original positions of each entry. The `get_hyper_index` method utilizes this index to deliver consistent results regardless of data changes.</br>

### File:
* `3-hypermedia_del_pagination.py`: Implements deletion-resilient pagination (`get_hyper_index`) ( + ).

