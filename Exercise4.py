from collections import namedtuple, defaultdict, OrderedDict, deque, ChainMap, Counter


# Word Frequency Counter:Given a text, use Counter to count the frequency of each word.
# Identify the most common word and its frequency.
def word_with_high_freq(text):
    list = text.split(" ")
    count = Counter(list)
    c = count.most_common(1)
    print(
        f"Most common word in the give text is {c[0][0]} and its frequency is {c[0][1]}"
    )


text = "hello i am hello how are you doing hello "
word_with_high_freq(text)


# Grouping Items:Given a list of tuples representing (name, category), use defaultdict to group the names by category.
def group_by_category(tuple_list):
    result = defaultdict(list)
    for tuple in tuple_list:
        result[tuple[1]].append(tuple[0])
    print(result)
    print(result["yehhdh"])


data = [
    ("Alice", "Technology"),
    ("Bob", "Science"),
    ("Charlie", "Technology"),
    ("David", "Science"),
    ("Eva", "Art"),
    ("Frank", "Art"),
]
group_by_category(data)


# Ordered Dictionary:Create an OrderedDict with keys as days of the week and values as corresponding activities.
# Print the dictionary and observe the order.
day_wise_activities = OrderedDict()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activities = [
    "Gardening",
    "Hiking",
    "Badminton",
    "Scuba-diving",
    "Dancing",
    "Cooking",
    "Photography",
]
for day, activity in zip(days, activities):
    day_wise_activities[day] = activity
print(day_wise_activities)

# Namedtuple for Coordinates:Define a namedtuple called Point with fields ‘x’ and ‘y’.
# Create instances of Point representing different coordinates.
Point = namedtuple("Point", ["x", "y"])
coordinate1 = Point(x=4, y=6)
print(coordinate1)


# Deque Operations:Use a deque to implement a simple stack (last-in, first-out).
class stack_using_deque:
    def __init__(self):
        self.stack = deque()

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if not self.isEmpty():
            print(f"popping the element {self.stack[0]}")
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


st = stack_using_deque()
st.push(78)
st.push(7)
print(f"stack is {st.stack}")


# Implement a queue (first-in, first-out) using a deque.
class queue_using_deque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, num):
        self.queue.append(num)

    def pop(self):
        if not self.is_empty():
            print(f"Popping the element {self.queue[0]}")
            return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


queue_object = queue_using_deque()
queue_object.enqueue(89)
queue_object.enqueue(78)
queue_object.enqueue(45)
queue_object.pop()
print(f"Queue is {queue_object.queue}")

# Combining Dictionaries:Create two dictionaries representing settings with default values.
# Use ChainMap to combine them, giving preference to the second dictionary for non-default values.
dict1 = {"theme": "dark", "color": "pink", "font": "16px"}
dict2 = {"theme": "light", "color": "red", "font-family": "Sanserif"}
chained_dict = ChainMap(dict2, dict1)
print(f"Chained dict is {chained_dict}")
print(chained_dict["theme"])


# namedtuple (advanced):
# Extending namedtuple:Create a namedtuple called Person with fields ‘name’, ‘age’, and ‘gender’.
# Extend it to include a method that returns a greeting based on the person’s gender.

Person = namedtuple("Person", ["name", "age", "gender"])


class ExtendedPerson(Person):
    def greeting(self):
        if self.gender == "Male":
            return f"Hello Mr {self.name}"
        elif self.gender == "Female":
            return f"Hello Miss {self.name}"
        else:
            return f"hello {self.name}"


person1 = ExtendedPerson("Amrutha", 28, "female")
print(person1.greeting())


# Common Elements Counter:Given two lists, use Counter to find the common elements and their frequencies.
def find_common_words(list1, list2):
    dict1 = Counter(list1)
    dict2 = Counter(list2)
    dict3 = {}
    for word in set(list1).intersection(set(list2)):
        dict3[word] = min(dict1[word], dict2[word])
    return dict3


list1 = ["hii", "hello", "hii", "hello"]
list2 = ["hey", "hello", "hello", "hii"]
common_words_dict = find_common_words(list1, list2)
print(f"counter with common elements and frequency is {common_words_dict}")

# Nested defaultdict:Implement a nested dictionary using defaultdict to store information about students and their grades in different subjects.
Students = defaultdict(lambda: defaultdict(str))
Students["Alice"]["Python"] = "a"
Students["Bob"]["React"] = "b"
print("Dictionary is ", Students)
