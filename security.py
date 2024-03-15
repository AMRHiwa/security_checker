# The program is developed by Mohammad Rasul Azizi 
# winter 2024


# Calling a Regex module to review a format in the text.
import re

# define a class 
class Security:
    
    # Definition of the original function to receive and decrypted
    def secure(self, info: str) -> str:

        # Divide the input parameter into words through the distance between them
        texts = info.split()

        # Create a variable for the output parameter
        final_ouput_param = []
        
        # Navigation of words
        for text in texts:

            # Checking the valid address of a social network
            if self.is_social_account_info(text):

                # Define a pattern to finde social network username
                pattern = r"[A-Z][\w]*:www.[\w\d\.]+\/([\w\d_]*)"

                # Find a username using defined pattern
                user = re.findall(pattern, text)

                # Add the text -placed text from decoding the username to the variable Final_oupu_param
                final_ouput_param.append(text.replace(user[0], self.encrypt(user[0])))

                # Back to the first loop
                continue

            # Add the text to the variable Final_output_param
            final_ouput_param.append(text)
        
        # The annexation of all the texts within the variable Final_utput_param and turned back to the program
        return ' '.join(final_ouput_param)

    # define the function for checking valid or not valid a social media address
    def is_social_account_info(self, param: str) -> bool:

        # define a pattern for social media address
        pattern = r"[A-Z][\w]*:www.[\w\d\.]+\/[\w\d_]*"

        # If the pattern is compatible with the input parameter, send the TRUE phrase to the program.
        if re.match(pattern, param):
            return True

        # If the condition is not made, the FALSE value will return to the program.
        else:
            return False

    # Definition of a function for decrypting username
    def encrypt(self, s: str) -> str:

        # Add a distance to the end of the input parameter
        s = s + ' '
        
        # Create an empty list to put the input text pieces
        temp_cutting = list()

        # Create a loop until the input text size greater than 1
        while len(s) > 1:

            # Definition of Index
            index = 0

            # Define a variable to store the current character's index for pointer
            current_letter_index = index

            # Define a variable to save the current characters
            curent_letter = s[0]

            # Definition of a variable to store the next characters' index
            next_letter_index = index + 1

            # Survey of Input text letters from the second letter to the end
            for letter in s[1:]:

                # If the current letter is the same as the character in the curent_letter variable
                if curent_letter == letter:
                    
                    #  add a unit to the Next_letter_index variable.
                    next_letter_index += 1
                
                else:
                
                    # Definition of Last_letter_index variable to save the last letter index
                    last_letter_index = next_letter_index

                    # Adding the separated section of the text from the current characters to the end of the characters
                    temp_cutting.append(s[current_letter_index:last_letter_index])

                    # Reduce the separated section of the input text
                    s = s[last_letter_index:]

                    # Exit from the loop
                    break
        
        # Create an empty dictionary to decrypt words
        decrypt_uniform = dict()

        # Survey of the words inside Temp_cutting
        for item in temp_cutting:

            # Definition of an empty string variable for decoding
            decrypt = ''

            # Definition of a counter -letter from number 1
            count = 1

            # Navigation of the word letters
            for letter in item:

                # Add the Ord code each letter to the decoded string
                decrypt += str((ord(letter)-96)*count)

                # Add to the counter
                count += 1
            
            # Add the word along with decoding it to the dictionary
            decrypt_uniform.update({item: decrypt})

        # Annexing the decoded texts together and storing them
        final_decrypt = ''.join(decrypt_uniform.values())

        # Return decoded text to the application
        return final_decrypt

security = Security()
print(security.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi'))