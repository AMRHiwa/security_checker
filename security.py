# The program is developed by Mohammad Rasul Azizi 
# winter 2024


# Calling a Regex module to review a format in the text.
import re

# define a class 
class Security:

    def secure(self, info):
        texts = info.split()
        final_ouput_param = []
        for text in texts:
            if self.is_social_account_info(text):
                pattern = r"[A-Z][\w]*:www.[\w\d\.]+\/([\w\d_]*)"
                user = re.findall(pattern, text)
                final_ouput_param.append(text.replace(user[0], self.encrypt(user[0])))
                continue
            final_ouput_param.append(text)
        return ' '.join(final_ouput_param)

    # define the function for checking valid or not valid a social media address
    def is_social_account_info(self, param):

        # define a pattern for social media address
        pattern = r"[A-Z][\w]*:www.[\w\d\.]+\/[\w\d_]*"

        # If the pattern is compatible with the input parameter, send the TRUE phrase to the program.
        if re.match(pattern, param):
            return True

        # If the condition is not made, the FALSE value will return to the program.
        else:
            return False

    def encrypt(self, s):
        s = s + ' '
        temp_cutting = list()
        while len(s) > 1:
            index = 0
            current_letter_index = index
            curent_letter = s[0]
            next_letter_index = index + 1
            for letter in s[1:]:
                if curent_letter == letter:
                    next_letter_index += 1
                else:
                    last_letter_index = next_letter_index
                    temp_cutting.append(s[current_letter_index:last_letter_index])
                    s = s[last_letter_index:]
                    break
        decrypt_uniform = dict()
        for item in temp_cutting:
            decrypt = ''
            count = 1
            for letter in item:
                decrypt += str((ord(letter)-96)*count)
                count += 1
            decrypt_uniform.update({item: decrypt})
        final_decrypt = ''.join(decrypt_uniform.values())
        return final_decrypt

security = Security()
print(security.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi'))