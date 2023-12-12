def feel_good(part_3):
    """For the different genres in the 'feel good' category, different inputs will give different 
    movie suggestions. 
    
    Parameter: part_ (user input, str)
    Return: Move reccomendation in str form"""
        
        
    comedy_movs = ['Napoleon Dynamite (82 min)', 'Nacho Libre (92 min)', 'Scott Pilgrim vs. The World (112 min)'] 
    rom_movs = ['10 Things I Hate About You (97 min)', 'Pride and Prejudice (127 min)', "She's The Man (105 min)"]
    musical_movs = ['La La Land (128 min)', 'Tik, Tik...Boom (115 min)', 'Mamma Mia! (108 min)']
    
    
    if part_3 == 'comedy':
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film with some action?")
        part_a = input('Y OR N :\t')
        
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + comedy_movs[2] + ' ☜╮(◠ ‿ ◠✿)')
                
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film with some cringe...but funny moments?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + comedy_movs[0] + ' ☜╮(◠ ‿ ◠✿)')
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film with some heart-warming moments?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + comedy_movs[1] + ' ☜╮(◠ ‿ ◠✿)')
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
              
                
        else:
            print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
 

        
        
        
        
        
      
    elif part_3 == 'romance':
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film with an enemies to lovers trope?")
        part_a = input('Y OR N :\t')
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + rom_movs[0] + ' ☜╮(◠ ‿ ◠✿)')
                
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a classic film that is a romantic period-piece?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + rom_movs[1] + ' ☜╮(◠ ‿ ◠✿)')
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film with a complicated love-triangle?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + rom_movs[2] + ' ☜╮(◠ ‿ ◠✿)')
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                          
                
        else:
            print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")

        
        
      
        
        

    elif part_3 == 'musical':
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film full of love and dreams?")
        part_a = input('Y OR N :\t')
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + musical_movs[0] + ' ☜╮(◠ ‿ ◠✿)')
                
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a classic film based on a real life story?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + musical_movs[1] + ' ☜╮(◠ ‿ ◠✿)')
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film with some confusion and laughable drama?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + musical_movs[2] + ' ☜╮(◠ ‿ ◠✿)')
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                           
                
    else:
        print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
          
        
        
        