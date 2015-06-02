
def generate_lesson_HTML(lesson_title, lesson_topic, lesson_notes):
     # I had to simplify my html here becuase I was having a very dificult time with the python sturcture.  I tried and tried to build it like my html notes but
     # I was getting a little frustrated with the trial and error corrections. I took an extra week here just because the python structure wasn't sinking in.
     # I'm starting to understand how this section flows but in no way am I an expert.
    html_text_1 = '''
    <div class="lesson"> 
        <div class="sections">        
            <div class="lesson-topics">
                '''+ lesson_topic
    html_text_2 = '''
            </div>
            <div class="lesson-notes">
                ''' + lesson_notes
    html_text_3 = '''
            </div>
        </div>
    </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(lesson):
    start_location = lesson.find('TITLE:')
    end_location = lesson.find('TITLE:')
    title = lesson[start_location+7 : end_location-1]
    return title

def get_topic(lesson):
    start_location = lesson.find('TOPIC:')
    end_location = lesson.find('NOTES:')
    topic = lesson[start_location+7: end_location-1]
    return topic

def get_notes(lesson):
    start_location = lesson.find('NOTES:')
    NOTES = lesson[start_location+7:]
    return NOTES

def get_lesson_by_number(text, lesson_number):
    counter = 0
    while counter < lesson_number:
        counter = counter + 1
        next_lesson_start = text.find('TOPIC:')
        next_lesson_end   = text.find('TOPIC:', next_lesson_start + 1)
        if next_lesson_end >= 0:
            lesson = text[next_lesson_start:next_lesson_end]
        else:
            next_lesson_end = len(text)
            lesson = text[next_lesson_start:]
        text = text[next_lesson_end:]
    return lesson

HTML_NOTES = """
                        TOPIC: A Computer
                        NOTES: Referencing back to stage 1 we mentioned computers are stupid.
                        Well, they really are. A computer will just sit there until we tell it what to do.
                        A computer can be programmed to do anything we want.
                        All we have to do is write a properly structured program and run it.
                        
                        TOPIC: A Computer Program
                        NOTES: A program comes in many forms and uses.
                        Actually, as soon as you turn on any computer or device you are running some kind of program.
                        Email, web browsing, browser and mobile app are all programs.
                        
                        TOPIC: Programming Language
                        NOTES: This language is what is used to tell a computer what to do.
                        The programming language was developed to eliminate language ambiguity.
                        From person to persons and country to country things we say could have different meaning.
                        Regular language interpretation could be an issue for computing. The language we are going to use is Python.
                                    
                        TOPIC: Python
                        NOTES: Python is a programming language interpreter.
                        When you write your code Python converts that code to instruction a computer can act on.
                        Sounds easy right? Well, keeping in mind your computer is stupid you must use proper grammar.
                        When using Python you must use the exact code in order for the interpreter to run the code. 
                        Backus-Naur Form describes python language rule.
                        It is a formal, mathematical way to specify context-free grammars that is both precise and unambiguous.<br>
                        A fun little article can be found <a href="http://matt.might.net/articles/grammars-bnf-ebnf/">here</a>.

                        TOPIC: Expressions
                        NOTES: Python interpreter is a language and only knows how to evaluate code that is part of the python language.
                        If something is written that isn't part of the language it will generate a syntax error. Python grammar uses expressions.
                        Python grammar uses expressions. 
                        Replacement grammar for arithmetic expression structure.

                        """


def generate_all_html(text):
    current_lesson_number = 1
    lesson = get_lesson_by_number(text, current_lesson_number)
    all_html = ''
    while lesson != '':
        title = get_title(lesson)
        topic = get_topic(lesson)
        notes = get_notes(lesson)
        lesson_html = generate_lesson_HTML(title, topic, notes)
        all_html = all_html + lesson_html
        current_lesson_number = current_lesson_number + 1
        lesson = get_lesson_by_number(text, current_lesson_number)
    return all_html


print generate_all_html(HTML_NOTES)

#----------------Having a go at generating from lists--------------------------------

def generate_lesson_HTML(lesson_title, lesson_topic, lesson_notes):
     
    html_text_1 = '''
    <div class="lesson">
    
        <div class="sections">
            ''' + lesson_title
    html_text_2='''
            <div class="lesson-topics">
                '''+ lesson_topic
    html_text_3 = '''
            </div>
            <div class="lesson-notes">
                ''' + lesson_notes
    html_text_4 = '''
            </div>
        </div>
    </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

def make_HTML(notes):
    
    lesson_title = notes[0]

    lesson_topic = notes[1]

    lesson_notes = notes[2]

    return generate_lesson_HTML(lesson_title, lesson_topic, lesson_notes)


# OK I'm sure there is a better way to do this than what I've just done here. Generating html from lists is a little easier than the previous section using get and loops. Yes, I did a tone of google lookup. This isn't all stuck in my head for sure yet. 
LIST_OF_NOTES = [ ["Lesson 2.2: Variables and Strings", "", ""],
                  ["", "What is a variable?", "Python allows you to create variables. We can use a variable to create a name and then use the name to refer to a variable."], #How do your wrap this back so my list doesn't go off the page?
                  ["", "What does it mean to assign a value to a variable?", "Being able to assign variables is a benefit in many ways. For me the biggest I see is a time saver. Being able to assign a name (variable) to repetitive entries or tasks or even just long numbers that are hard to remember like the speed of light is huge and helps understand what you just did. Keeping your statements meaningful helps too.<br>The question which side of = is evaluated first? The right side is looked at first. In this days = 49 you could say I'm taking 49 and assigning it to days."],
                  ["", "Strings", "Strings are a sequence of characters in quotes. Can be single or double but needs to be consistent."] ]


def make_HTML_for_several_notes(list_of_notes):

    HTML = ""

    for notes in list_of_notes:

        notes_HTML = make_HTML(notes)

        HTML = HTML + notes_HTML

    return HTML

print make_HTML_for_several_notes(LIST_OF_NOTES)

# Yes it's time for a drink 




