import re

class Security:

    def secure(self, info):
        texts = info.split()
        # decrypted_user = dict()
        final_ouput_param = []
        for text in texts:
            if self.is_social_account_info(text):
                pattern = r"[A-Z][\w]*:www.[\w\d\.]+\/([\w\d_]*)"
                user = re.findall(pattern, text)
                # print(type(user[0]))
                # decrypted_user.update({user[0]: self.encrypt(user[0])})
                final_ouput_param.append(text.replace(user[0], self.encrypt(user[0])))
                continue
            final_ouput_param.append(text)
        return ' '.join(final_ouput_param)
        # print(decrypted_user)
        # print(final_ouput_param)

    def is_social_account_info(self, param):
        pattern = r"[A-Z][\w]*:www.[\w\d\.]+\/[\w\d_]*"
        if re.match(pattern, param):
            return True
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
# print( security.encrypt('abcccdd'))
# print( security.is_social_account_info('Twitter:www.twitter.com/javalover1990'))
print(security.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi'))