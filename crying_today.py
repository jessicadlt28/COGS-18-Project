def crying_today(part_4):
    
    """For the different genres in the 'crying today' category, different inputs will give different 
    movie suggestions. 
    
    Parameter: part_4 (user input, str)
    Return: Move reccomendation in str form"""
    
    drama_movs = ['The Lovely Bones (135 min)', 'Moonlight (111 min)', 'Precious (109 min)']
    bitt_movs = ['Aftersun (96 min)', 'Miracle In Cell No. 7 (145 min)', 'The Notebook (113 min)']
    docu_movs = ['The Three Deaths of Marisela Escobedo (109 min)', 'Dear Zachary: A Letter To His Son About His Father (95 min)', "Bulgaria's Abandoned Children (60 min)"]
    
    
    if part_4 == 'drama':
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film based on a true crime story ?")
        part_a = input('Y OR N :\t')
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + drama_movs[0] + ' ☜╮(◕﹏◕)')
                  
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film that revolves around boyhood and masculinity?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y' or 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + drama_movs[1] + ' ☜╮(◕﹏◕)')
                
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film that portrays the challenging life experiences of a woman in NYC?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + drama_movs[2] + ' ☜╮(◕﹏◕)')
                    
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
              
                
        else:
            print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
        
       
        
        
                
    elif part_4 == 'documentary':
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film that focuses on the feminicide in Mexico?")
        part_a = input('Y OR N :\t')
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + docu_movs[0] + ' ☜╮(◕﹏◕)')
                  
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film crime, custody, and remembrance?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + docu_movs[1] + ' ☜╮(◕﹏◕)')
                
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film that centers around experiences of children in developing countries?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + docu_movs[2] + ' ☜╮(◕﹏◕)')
                    
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                          
                
        else:
            print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
        

        
        
        

    elif part_4 == 'bittersweet':
        print("FILMSICAL: Let's get some more info on your movie likes! Pls reply to the questions with a 'Y' or 'N'. ")
        
        print("FILMSICAL: Do you want a film centered on family relationships?")
        part_a = input('Y OR N :\t')
        
        if part_a in ['Y', 'y']:
            print("FILMSICAL: Oooh! Great choice! Here's an option: " + bitt_movs[0] + ' ☜╮(◕﹏◕)')
                  
        elif part_a in ['N', 'n']:
            print("FILMSICAL: OK. How about a film that will have you go from smiling to bawling?")
            part_b = input('Y OR N :\t')
                
            if part_b in ['Y', 'y']:
                print("FILMSICAL: Oooh! Great choice! Here's an option: " + bitt_movs[1] + ' ☜╮(◕﹏◕)')
                
            elif part_b in ['N', 'n']:
                print("FILMSICAL: OK. How about a film that will have you questioning 'love'?")
                part_c = input('Y OR N :\t')
                        
                if part_c in ['Y', 'y']:
                    print("FILMSICAL: Oooh! Great choice! Here's an option: " + bitt_movs[2] + ' ☜╮(◕﹏◕)')
                    
                elif part_c in ['N', 'n']:
                    print("FILMSICAL: OK. Seems like this may not be the right genre for you, bye.")
                      
                
    else:
        print("FILMSICAL: Ooops. I can't accept your response, bye. (●__● )")
       
        
         
        
        