### App Design\

- Category
  -> OS
  -> Color
  -> Brand
  -> Price
  - RAM 
  - Camera - MP, types of lens
  - Screen Res
  - Refresh Rate

- Products
  - Features listed in category
  - Samsung 
  - Apple

- Customer
  - Should extend `AbstractUser` model. Create a custom `UserCreationForm` and `UserChangeForm`
    - Abstract user -> Create Model -> Create Forms 
  - Is this model for user authentication
    - login
    - singup (using OTP)
      - registers phone number 
  - first name
  - last name
  - email
  - phone number
  - password