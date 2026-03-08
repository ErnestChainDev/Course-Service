import os
import json
from dotenv import load_dotenv

from shared.database import build_mysql_url, make_engine, make_session_factory, Base
from .models import Course

load_dotenv()

db_url = build_mysql_url(
    host=os.environ["MYSQLHOST"],
    port=os.environ["MYSQLPORT"],
    user=os.environ["MYSQLUSER"],
    password=os.environ["MYSQLPASSWORD"],
    db=os.environ["MYSQLDATABASE"],
)

engine = make_engine(db_url)
SessionLocal = make_session_factory(engine)

Base.metadata.create_all(bind=engine)

COURSES = [
    {
        "code": "CS101",
        "title": "Introduction to Programming",
        "description": "Learn the foundations of programming, problem-solving, logic building, variables, conditions, loops, and functions using beginner-friendly explanations.",
        "program": "BSCS",
        "level": "1st Year",
        "tags": "Programming, Logic, Problem Solving, Beginner Coding",
        "lessons": [
            {
                "title": "What is Programming?",
                "content": "Programming is the process of creating instructions that a computer can follow in order to perform a task. These instructions are written using a programming language such as Python, Java, C++, or JavaScript. A computer does not understand human language the way people do, so programmers write clear and logical commands that the machine can interpret step by step.\n\nProgramming is important because it is used in almost every part of modern life. Websites, mobile apps, banking systems, social media platforms, school portals, games, and smart devices all depend on programming. When you learn programming, you learn how to think in a structured way and how to break a problem into smaller parts that are easier to solve.\n\nA programmer does not only write code. A programmer also studies the problem, plans a solution, tests the output, and fixes errors. This means programming is both technical and creative. It requires logical thinking, patience, and continuous practice."
            },
            {
                "title": "Programming Languages and Basic Syntax",
                "content": "A programming language is a formal way of writing instructions for a computer. Different languages are used for different purposes. Python is known for being beginner-friendly and easy to read. Java is often used in enterprise systems and Android development. JavaScript is widely used in web development.\n\nAlthough languages are different, many of them share common ideas. They use variables, conditions, loops, input, output, and functions. The syntax of a programming language refers to the rules for writing valid code. If the syntax is wrong, the program may not run properly."
            },
            {
                "title": "Variables and Data Types",
                "content": "Variables are named storage locations used to keep data in a program. They allow programmers to store values that can be changed and reused. Data types describe the kind of value stored in a variable, such as integers, strings, booleans, and floating-point numbers.\n\nVariables make programs dynamic. Instead of writing the same value every time, a programmer can use a variable and update it whenever needed."
            },
            {
                "title": "Input and Output",
                "content": "Input and output are basic parts of almost every program. Input refers to data that the user provides to the computer. Output refers to the information that the computer shows or returns after processing the input.\n\nA beginner should understand that input and output help connect the user to the logic of a program."
            },
            {
                "title": "Conditional Statements",
                "content": "Conditional statements allow a program to make decisions. They let the program choose what action to take depending on whether a condition is true or false. Common conditional structures include if, else if, and else statements."
            },
            {
                "title": "Loops and Repetition",
                "content": "Loops are structures that repeat a block of code multiple times. Instead of writing the same instructions again and again, a programmer uses a loop to perform repetition automatically."
            },
            {
                "title": "Functions and Problem Solving",
                "content": "A function is a reusable block of code designed to perform a specific task. Functions help organize a program into smaller and clearer parts. Problem solving is at the heart of programming."
            },
        ],
    },
    {
        "code": "IT201",
        "title": "Web Development Fundamentals",
        "description": "Study how websites are built using HTML, CSS, and JavaScript, including page structure, styling, responsiveness, and interactivity.",
        "program": "BSIT",
        "level": "2nd Year",
        "tags": "HTML, CSS, JavaScript, Frontend, Web Design",
        "lessons": [
            {"title": "Introduction to Web Development", "content": "Web development is the process of building websites and web applications that users can access through a browser. It includes designing the layout, creating the structure of pages, adding styles, and building interactive features."},
            {"title": "HTML Structure and Semantic Elements", "content": "HTML stands for HyperText Markup Language. It is used to create the structure of a webpage. Semantic elements help describe the purpose of each part of the page."},
            {"title": "CSS Styling and Layout", "content": "CSS stands for Cascading Style Sheets. It is used to control the appearance of HTML elements. CSS helps create layouts, colors, spacing, and professional-looking interfaces."},
            {"title": "Responsive Design", "content": "Responsive design means building webpages that adapt well to desktops, tablets, and mobile phones."},
            {"title": "JavaScript Basics and DOM Manipulation", "content": "JavaScript is the programming language used to add interactivity to webpages. It allows developers to respond to clicks and change page content dynamically."},
            {"title": "Forms and User Interaction", "content": "Forms allow users to submit data such as login details, feedback, and profile information."},
            {"title": "Frontend Best Practices", "content": "Frontend best practices include writing clean code, organizing files properly, and designing for accessibility and performance."},
        ],
    },
    {
        "code": "IS202",
        "title": "Database Management Systems",
        "description": "Understand database concepts, data organization, relationships, normalization, and SQL operations for storing and retrieving information effectively.",
        "program": "BSIS",
        "level": "2nd Year",
        "tags": "Database, SQL, ERD, Tables, Data Management",
        "lessons": [
            {"title": "Introduction to Databases", "content": "A database is an organized collection of data stored in a way that allows efficient access, retrieval, and management."},
            {"title": "Tables, Rows, Columns, and Keys", "content": "Relational databases organize data into tables. Keys are special fields used to identify and connect records."},
            {"title": "Relationships and Entity Design", "content": "Relationships describe how tables are connected in a database. Designers often use ERDs to plan database structure."},
            {"title": "SQL Basics", "content": "SQL stands for Structured Query Language. It is used to create, read, update, and delete data in relational databases."},
            {"title": "Normalization and Data Integrity", "content": "Normalization is the process of organizing data to reduce redundancy and improve consistency."},
            {"title": "Queries, Filtering, and Reporting", "content": "Queries help retrieve useful information from a database using filters, sorting, grouping, and joins."},
            {"title": "Database Security and Maintenance", "content": "Database security protects data from unauthorized access, while maintenance helps preserve performance and reliability."},
        ],
    },
    {
        "code": "CS301",
        "title": "Data Structures and Algorithms",
        "description": "Learn how data is organized and processed efficiently using arrays, linked lists, stacks, queues, trees, sorting, searching, and algorithm analysis.",
        "program": "BSCS",
        "level": "3rd Year",
        "tags": "Algorithms, Data Structures, Efficiency, Problem Solving",
        "lessons": [
            {"title": "Introduction to Data Structures and Algorithms", "content": "Data structures organize data efficiently. Algorithms are step-by-step procedures used to solve problems."},
            {"title": "Arrays and Linked Lists", "content": "Arrays and linked lists are fundamental ways of storing collections of data."},
            {"title": "Stacks and Queues", "content": "Stacks use LIFO, while queues use FIFO. Both are widely used in real systems."},
            {"title": "Trees and Hierarchical Data", "content": "Trees are hierarchical structures useful for representing folders, menus, and structured information."},
            {"title": "Searching and Sorting Algorithms", "content": "Searching algorithms locate values, while sorting algorithms arrange data in order."},
            {"title": "Algorithm Efficiency and Big-O Notation", "content": "Big-O notation describes how efficiently an algorithm performs as input size grows."},
            {"title": "Applying Data Structures to Real Problems", "content": "Real systems combine multiple data structures and algorithms to solve practical problems."},
        ],
    },
    {
        "code": "IT305",
        "title": "Networking Basics",
        "description": "Explore the essentials of computer networking, devices, IP addressing, protocols, communication models, and troubleshooting.",
        "program": "BSIT",
        "level": "3rd Year",
        "tags": "Networking, IP Address, Router, Protocols, Internet",
        "lessons": [
            {"title": "Introduction to Computer Networks", "content": "A computer network is a group of connected devices that can communicate and share resources."},
            {"title": "Network Types and Topologies", "content": "Networks can be classified by size and arranged using different topologies such as star and mesh."},
            {"title": "Network Devices", "content": "Routers, switches, modems, and access points are common network devices with different roles."},
            {"title": "IP Addressing and Subnet Basics", "content": "An IP address uniquely identifies a device on a network. Subnetting divides a network into smaller sections."},
            {"title": "Protocols and Communication", "content": "Protocols define the rules used by devices to communicate over a network."},
            {"title": "Basic Network Security", "content": "Network security protects data, devices, and services from unauthorized access and attacks."},
            {"title": "Troubleshooting Common Network Problems", "content": "Troubleshooting helps identify and fix connectivity, configuration, and hardware problems."},
        ],
    },
    {
        "code": "TVE101",
        "title": "Educational Technology Tools",
        "description": "Learn how digital tools support teaching and learning through presentation tools, LMS platforms, collaboration apps, multimedia resources, and responsible technology use.",
        "program": "BTVTED",
        "level": "1st Year",
        "tags": "EdTech, LMS, Digital Tools, Teaching, Multimedia",
        "lessons": [
            {"title": "Introduction to Educational Technology", "content": "Educational technology refers to the use of digital tools, systems, and media to improve teaching and learning."},
            {"title": "Presentation and Content Creation Tools", "content": "Presentation tools help teachers deliver lessons in a visual and organized way."},
            {"title": "Learning Management Systems", "content": "An LMS helps teachers organize lessons, assignments, quizzes, grades, and communication."},
            {"title": "Collaboration and Communication Tools", "content": "Collaboration tools support teamwork, communication, and active learning."},
            {"title": "Multimedia and Interactive Learning", "content": "Multimedia uses text, audio, images, animation, and video to support better understanding."},
            {"title": "Assessment Tools and Feedback", "content": "Digital assessment tools help teachers evaluate student understanding and provide feedback."},
            {"title": "Responsible and Ethical Use of Technology", "content": "Technology should be used responsibly, ethically, safely, and inclusively in education."},
        ],
    },
]


def seed_courses():
    db = SessionLocal()
    try:
        for item in COURSES:
            existing = db.query(Course).filter(Course.code == item["code"]).first()
            if existing:
                print(f"Skipping existing course: {item['code']} - {item['title']}")
                continue

            course = Course(
                code=item["code"],
                title=item["title"],
                description=item["description"],
                program=item["program"],
                level=item["level"],
                tags=item["tags"],
                lessons=json.dumps(item["lessons"], ensure_ascii=False),
            )
            db.add(course)
            print(f"Added: {item['code']} - {item['title']}")

        db.commit()
        print("Seeding completed successfully.")
    except Exception as e:
        db.rollback()
        print("Seeding failed:", e)
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_courses()