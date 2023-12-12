def shook_core(part_5):
    """For the different genres in the 'shook to my core' category, different inputs will give different 
    movie suggestions. 
    
    Parameter: part_5 (user input, str)
    Return: Move reccomendation in str form"""
    
    mystery_movs = ['The Butterfly Effect (120 min)', 'Donnie Darko (113 min)', 'Triangle (99 min)']
    thrill_movs = ['Midsommar (148 min)', "I'm Thinking of Ending Things (134 min)", 'Parasite (132 min)']
    dyst_movs = ['Interstellar (169 min)', 'The Hunger Games (142 min)', 'The Matrix (136 min)']
    
    
    if part_5 == 'thriller':
        
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film with plot twists that cover themes of relationships and grief?")
        part_a = input('Y OR N :\t')
        
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + thrill_movs[0] + '☜╮(•_• )')
                
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film with a shocking and unexpected ending?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + thrill_movs[1] + '☜╮(•_• )')
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film that starts off quite slow then becomes more intense?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + thrill_movs[2] + '☜╮(•_• )')
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                           
                
        else:
            print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
     
                
                
                
                
                
    elif part_5 == 'dystopian':
        
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a long film that seems understandble at first but then completely shocks you?")
        part_a = input('Y OR N :\t')
        
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + dyst_movs[0] + '☜╮(•_• )')
                
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film with that will make you experiences multiple emotions at once?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + dyst_movs[1] + '☜╮(•_• )')
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film that is giving futuristic vibes with lots of action?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + dyst_movs[2] + '☜╮(•_• )')
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                        
                
        else:
            print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
      

   
        
        
    elif part_5 == 'mystery':
        
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film that deals with time travel and trauma?")
        part_a = input('Y OR N :\t')
        
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + mystery_movs[0] + '☜╮(•_• )')
                
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film with an unexpected character causing issues?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + mystery_movs[1] + '☜╮(•_• )')
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film that will have you questioning your perception of the events?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + mystery_movs[2] + '☜╮(•_• )')
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                          
                
    else:
        print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
           

        
        
        
        