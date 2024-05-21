# 🚀 0x01. Caching 🗃️💾 
`Back-end`

## Background Context
In this project, you will learn about different caching algorithms and their implementations.
<br></br>

## Resources
Read or watch:</br>
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_(LFU))
<br></br>

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:</br>
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system is
- What limits a caching system has
<br></br>

## Requirements
### Python Scripts
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- Documentation should not be a simple word but a real sentence explaining the purpose of the module, class, or method
<br></br>

## More Info
### Parent class BaseCaching
All your classes must inherit from `BaseCaching` defined below:</br>

base_caching.py
```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Tasks
### Task 0. Basic dictionary
Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:</br>
- Use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have a limit
- `def put(self, key, item)`:
  - Assign to the dictionary `self.cache_data` the item value for the key `key`
  - If key or item is `None`, this method should not do anything
- `def get(self, key)`:
  - Return the value in `self.cache_data` linked to `key`
  - If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`

#### Task 0: Edge Test Case
**File:**
```python
0-main.py
```

**Test command:**
```bash
./0-main.py
```

Repo:</br>
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `0-basic_cache.py`

<br></br>

### Task 1. FIFO caching
Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:</br>
- Use `self.cache_data` - dictionary from the parent class `BaseCaching`
- Overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item)`:
  - Assign to the dictionary `self.cache_data` the item value for the key `key`
  - If key or item is `None`, this method should not do anything
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
    - Discard the first item put in cache (FIFO algorithm)
    - Print `DISCARD:` with the key discarded and following by a new line
- `def get(self, key)`:
  - Return the value in `self.cache_data` linked to `key`
  - If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`

#### Task 1: Edge Test Case
**File**
```python
1-main.py
```

**Test command**
```bash
./1-main.py
```

Repo:</br>
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `1-fifo_cache.py`

<br><br>

### Task 2. LIFO Caching
Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:</br>
- Use `self.cache_data` - dictionary from the parent class `BaseCaching`
- Overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item)`:
  - Assign to the dictionary `self.cache_data` the item value for the key `key`
  - If key or item is `None`, this method should not do anything
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
    - Discard the last item put in cache (LIFO algorithm)
    - Print `DISCARD:` with the key discarded and following by a new line
- `def get(self, key)`:
  - Return the value in `self.cache_data` linked to `key`
  - If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`

#### Task 2: Edge Test Case
**File**
```python
2-main.py
```

**Test command**
```bash
./2-main.py
```


Repo:</br>
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `2-lifo_cache.py`

<br></br>

### Task 3. LRU Caching
Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:</br>
- Use `self.cache_data` - dictionary from the parent class `BaseCaching`
- Overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item)`:
  - Assign to the dictionary `self.cache_data` the item value for the key `key`
  - If key or item is `None`, this method should not do anything
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
    - Discard the least recently used item (LRU algorithm)
    - Print `DISCARD:` with the key discarded and following by a new line
- `def get(self, key)`:
  - Return the value in `self.cache_data` linked to `key`
  - If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`

#### Task 3: Edge Test Case
**File**
```python
3-main.py
```

**Test command**
```bash
./3-main.py
```


Repo:</br>
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `3-lru_cache.py`

<br></br>

### Task 4. MRU Caching
Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:</br>
- Use `self.cache_data` - dictionary from the parent class `BaseCaching`
- Overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item)`:
  - Assign to the dictionary `self.cache_data` the item value for the key `key`
  - If key or item is `None`, this method should not do anything
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
    - Discard the most recently used item (MRU algorithm)
    - Print `DISCARD:` with the key discarded and following by a new line
- `def get(self, key)`:
  - Return the value in `self.cache_data` linked to `key`
  - If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`

#### Task 4: Edge Test Case
**File**
```python
4-main.py
```

**Test command**
```bash
./4-main.py
```


Repo:</br>
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `4-mru_cache.py`

<br></br>

### Task 5 (Advanced). LFU Caching
Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:</br>
- Use `self.cache_data` - dictionary from the parent class `BaseCaching`
- Overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item)`:
  - Assign to the dictionary `self.cache_data` the item value for the key `key`
  - If key or item is `None`, this method should not do anything
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
    - Discard the least frequently used item (LFU algorithm)
    - If you find more than one item to discard, use the LRU algorithm to discard only the least recently used
    - Print `DISCARD:` with the key discarded and following by a new line
- `def get(self, key)`:
  - Return the value in `self.cache_data` linked to `key`
  - If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`

#### Task 5 (Advanced): Edge Test Case
**File**
```python
2-main.py
```

**Test command**
```bash
./2-main.py
```


Repo:</br>
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `5-lfu_cache.py`

