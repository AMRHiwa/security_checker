# security_checker
This program has been developed by Mohammad Rasoul Azizi!

The program has tried to implement this template that decoded its username in an input text by looking for a specific virtual network address.

---

Encrypt method (Self, S)

A string is given as input of this method and its encrypted equivalent is returned to the output.

According to the following descriptions, we calculate the input encryption equivalent.

The string is first divided into its uniform subdivisions, and then the encrypted amount of the main string is obtained by gluing the encrypted amount of uniform strands.

By putting together the weight of all the uniforms of a string, a numerical phrase is obtained that is equivalent to the encryption of the input string.

The uniform is a string whose characters are the same.Such as C or AA or CCC.

For a unicorn string, the encryption value is obtained that for each character we add the character to the weight of the character in the number of characters previously mentioned, plus one to the end of the answer.(We start from the beginning of the field and go through it.)

For example, the encryption value of the CCCC uniform is 36912.

The weight of a character is equal to the numeric code of that character minus the number 96. 

For example, the character code A is 97 and its weight is 97−96 = 1.

---

Is_social_account_info method (Self, Param)

This method receives a string as an input parameter and specifies in the output whether the field contains an address for a social network account.At the time of recruitment, the Conservation and Security Unit asked the address of all public accounts and stored in the documents as follows:

[Social Network Name]: www\. [Domain]/[Account Name]

For example, Twitter Ali's account is as follows:

Twitter: www\.twitter\.com/javalover1990

Hints

The name of the social network always begins with the big English letter.

Domain only contains English lowercase letters and number and character.Is.

The account address contains the letter or number or the subcategory (_).

If the input field contains the address of a social network, the value of the TRUE should be returned and otherwise the FALSE value should be returned.

---

The secure method (Self, Info)

Now, using the previous two methods, we want to encrypt the information.As that:

Find sections that are related to user account information using the IS_social_account_info method.

Crypt the Account Name section using the Encrypt method.

**Example**

Input is a text that includes an employee information, including zero or more information on various social networks.

`FirstName: ali, LastName: Alavi, Birthdate: 1990/02/02 Gender: Male Instagram: www.instagram.com/aalavi Degree: Master Twitter: www.twiter.com/alaviii IMDB: www.imdb.com`


__Output__

`FirstName: ali, LastName: Alavi, Birthdate: 1990/02/02 Gender: Male Instagram: www.instagram.com/12121229 Degree: Master Twitter: www.twiter.com/11212291827 IMDB: www.imdb.com/`

