Welcome to E110!  "Engineering Computing Architecture" is about how computers are built from simpler components, and how they encode information into physical parts.  Along the way, we will also cover the Linux shell, Hardware Description Languages (HDL) and intermediate Python programming.

# Prerequisites
Students should have already taken ENGR-E 101 Innovation and Design: https://registrar.indiana.edu/browser/soc4192/ENGR/ENGR-E101.shtml

Students should also come to E110 prepared with:
- intermediate computer literacy
- editing, saving, and sharing documents
- working knowledge of Windows, MacOS, and/or Linux
- beginner experience in Python programming language (variables, functions, loops, lists)
- beginner experience with electronics (knowledge of transistors, microcontrollers, voltage, electricity)

# Outcomes
Students will finish E110 with knowledge in:
- fundamentals of digital logic (gates from transistors, complex gates from simple gates)
- how a CPU is constructed, as a system, from simpler components
- number representations (decimal, hexadecimal, binary)
- Linux command-line interface (CLI)
- MyHDL (hardware description language in the form of a Python library)
- intermediate Python

# People

| name            | role       | office     | email           |
|-----------------|------------|------------|-----------------|
| Alex Shroyer    | instructor | Luddy 4148 | ashroyer@iu.edu |
| Juliette Zerick | AI         | Luddy 4125 | jzerick@iu.edu  |
| Daniel Osei     | AI         | Luddy 4125 | dosei@iu.edu    |

# Classroom location, meeting times

| section | lecture           | lab                      | location   |
|---------|-------------------|--------------------------|------------|
|   10678 | (Mon) 10:10-11:00 | (Tues;Thurs) 11:15-12:30 | Luddy 4111 |
|   29714 | (Mon) 11:15-12:05 | (Tues;Thurs) 04:00-05:15 | Luddy 4111 |

# Office Hours

| time                | location   |
|---------------------|------------|
| (Tues) 01:00-02:00  | Luddy 4148 |
| (Thurs) 01:00-02:00 | Luddy 4148 |

# Announcements
We will post to Canvas with updates/clarifications/announcements.  By default, you should already have notifications from Canvas enabled.  It is your responsibility to ensure you can receive such announcements.

# Autograder
We will an automated grading system for assignments: [autograder link][autograder]

For security reasons, you must access it through the IU network - either access it while on campus, or use a [VPN] service to make the site think you're on campus.

# Materials/Textbooks
- Textbook: /The Elements of Computing Systems/ by Noam Nisan and Shimon Schocken. ISBN 978-0262640688
  This course covers chapters 1-6 of the [Nand to Tetris course]
- Python: Use the [docs for Python version 3.7.2 (latest stable release)][python3doc]
- MyHDL: [Manual](http://docs.myhdl.org/en/stable/) and [Examples](http://www.myhdl.org/docs/examples/)

# Conduct
**Lab/Classroom etiquette**

1. Respect others who want to work or listen quietly, minimize distractions.
2. No food or open drinks.  Non-spill bottles are OK.
3. Leave the lab at least as clean as you found it.
4. Log out before leaving.

**Do your own work**
Collaboration for learning and helping each other is encouraged, however all assignments must be exclusively _your own work_.  Cheating results in 0 credit for the assignment, reporting to the Dean, and possible further consequences.  Cheating also includes allowing others to copy your work.

See the [official IU policy] for more information.

**No late work**
You may submit multiple times to the Autograder; the highest scoring submission is the one that will be used in grading. No submissions after the deadline will be accepted. Sometimes the Autograder server may be heavily used and respond more slowly, so plan accordingly.

Extensions may, at the instructor's discretion, be given to _individuals_ in extreme circumstances, such as medical emergencies (Dr. note required).

**Disability Assistance**
If you require accommodations for a disability, please let your instructor know within the first 3 weeks of the semester.  As soon as we are aware of your needs, we can work with the Office of Disability Services for Students (DSS) to help determine appropriate academic accommodations.  Any information you share with us will be treated as confidential.

**Tutoring**
SICE tutoring is available to all students.

# Schedule
See also: [Official IU Calendar for Spring 2019][iucal]
 
| Date  | Day   | Topic                          | Reading                           | Assignment |
|-------|-------|--------------------------------|-----------------------------------|------------|
| 01/07 | Mon   | Intro, Linux CLI               | [Essential Linux Commands]        |            |
| 01/08 | Tues  | Python CLI, number conversion  | [Python builtin functions]        | [A00a]     |
| 01/10 | Thurs | Autograder practice            | MyHDL manual [M1], [M2], [M3]     | [A00b]     |
| 01/14 | Mon   | MyHDL, Boolean Logic           | [Ch1](Ch1) and [slides1](slides1) | [A01]      |
| 01/15 | Tues  | truth tables                   |                                   |            |
| 01/17 | Thurs | truth tables, continued        |                                   |            |
| 01/21 | Mon   | MLK Jr. Day                    |                                   |            |
| 01/22 | Tues  | Gates: 16-input and/or/etc.    | [Ch2](Ch2) and [slides2](slides2) |            |
| 01/24 | Thurs | Gates: Mux, Demux              |                                   |            |
| 01/28 | Mon   |                                |                                   | [A02]      |
| 01/29 | Tues  |                                |                                   |            |
| 01/31 | Thurs |                                |                                   |            |
| 02/04 | Mon   |                                |                                   | [A03]      |
| 02/05 | Tues  |                                |                                   |            |
| 02/07 | Thurs |                                |                                   |            |
| 02/11 | Mon   |                                | [Ch3](Ch3) and [slides3](slides3) | [A04]      |
| 02/12 | Tues  |                                |                                   |            |
| 02/14 | Thurs |                                |                                   |            |
| 02/18 | Mon   |                                |                                   | [A05]      |
| 02/19 | Tues  |                                |                                   |            |
| 02/21 | Thurs |                                |                                   |            |
| 02/25 | Mon   |                                | [Ch4](Ch4) and [slides4](slides4) | [A06]      |
| 02/26 | Tues  |                                |                                   |            |
| 02/28 | Thurs |                                |                                   |            |
| 03/04 | Mon   |                                |                                   | [A07]      |
| 03/05 | Tues  | Midterm Review                 |                                   |            |
| 03/07 | Thurs | Midterm - normal class time    |                                   |            |
| 03/11 | Mon   | Spring Break                   |                                   |            |
| 03/12 | Tues  | Spring Break                   |                                   |            |
| 03/14 | Thurs | Spring Break                   |                                   |            |
| 03/18 | Mon   |                                | [Ch5](Ch5) and [slides5](slides5) |            |
| 03/19 | Tues  |                                |                                   |            |
| 03/21 | Thurs |                                |                                   |            |
| 03/25 | Mon   |                                |                                   | [A08]      |
| 03/26 | Tues  |                                |                                   |            |
| 03/28 | Thurs |                                |                                   |            |
| 04/01 | Mon   |                                | [Ch6](Ch6) and [slides6](slides6) | [A09]      |
| 04/02 | Tues  |                                |                                   |            |
| 04/04 | Thurs |                                |                                   |            |
| 04/08 | Mon   |                                |                                   | [A10]      |
| 04/09 | Tues  |                                |                                   |            |
| 04/11 | Thurs |                                |                                   |            |
| 04/15 | Mon   |                                |                                   | [A11]      |
| 04/16 | Tues  |                                |                                   |            |
| 04/18 | Thurs |                                |                                   |            |
| 04/22 | Mon   |                                |                                   |            |
| 04/23 | Tues  | Final Review                   | None                              | None       |
| 04/25 | Thurs | Final Exam - normal class time | None                              | None       |
| 04/29 | Mon   | Finals Week                    |                                   |            |
| 04/30 | Tues  | Finals Week                    |                                   |            |
| 05/02 | Thurs | Finals Week                    |                                   |            |
| 05/06 | Mon   |                                |                                   |            |
| 05/07 | Tues  |                                |                                   |            |
| 05/09 | Thurs | Semester Ends                  |                                   |            |

[Essential Linux Commands]: https://beebom.com/essential-linux-commands/
[Python builtin functions]: https://docs.python.org/3/library/functions.html#int
[M1]: http://docs.myhdl.org/en/stable/manual/preface.html
[M2]: http://docs.myhdl.org/en/stable/manual/background.html
[M3]: http://docs.myhdl.org/en/stable/manual/intro.html
[iucal]: https://registrar.indiana.edu/official-calendar/official-calendar-spring.shtml?s=16w
[Ch1]: https://docs.wixstatic.com/ugd/44046b_f2c9e41f0b204a34ab78be0ae4953128.pdf
[Ch2]: https://docs.wixstatic.com/ugd/44046b_f0eaab042ba042dcb58f3e08b46bb4d7.pdf
[Ch3]: https://docs.wixstatic.com/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf
[Ch4]: https://docs.wixstatic.com/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf
[Ch5]: https://docs.wixstatic.com/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf
[Ch6]: https://docs.wixstatic.com/ugd/44046b_89a8e226476741a3b7c5204575b8a0b2.pdf
[A00a]: assignments/A00a.html
[A00b]: assignments/A00b.html
[slides1]: https://drive.google.com/file/d/1MY1buFHo_Wx5DPrKhCNSA2cm5ltwFJzM/view
[slides2]: https://docs.wixstatic.com/ugd/56440f_2e6113c60ec34ed0bc2035c9d1313066.pdf
[slides3]: https://docs.wixstatic.com/ugd/56440f_3b9f5721e3e149fba8687847da395c43.pdf
[slides4]: https://docs.wixstatic.com/ugd/56440f_12f488fe481344328506857e6a799f79.pdf
[slides5]: https://docs.wixstatic.com/ugd/56440f_96cbb9c6b8b84760a04c369453b62908.pdf
[slides6]: https://docs.wixstatic.com/ugd/56440f_65a2d8eef0ed4e0ea2471030206269b5.pdf
[VPN]: https://kb.iu.edu/d/ajrq
[official IU policy]: http://studentcode.iu.edu/responsibilities/academic-misconduct.html
[autograder]: https://autograder.sice.indiana.edu 
[Nand to Tetris course]: https://www.nand2tetris.org/course
[docs for Python version 3.7.2 (latest stable release)]: https://docs.python.org/3/
