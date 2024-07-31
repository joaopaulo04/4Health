from flet import *
from datetime import datetime
from features.User import User


def validate_cpf(cpf):
    # Remove qualquer caractere que não seja dígito
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # Verifica se o primeiro dígito verificador está correto
    if int(cpf[9]) != digito_verificador_1:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verifica se o segundo dígito verificador está correto
    if int(cpf[10]) != digito_verificador_2:
        return False

    return True


bool_bar1 = False

bool_bar2 = False


def signin(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def send_register(e):
        valid = True
        error_messages = []

        # Validação do nome
        name = name_textfield.value.strip()  # Remove espaços em branco
        if len(name) < 3 or len(name) > 50:
            valid = False
            error_messages.append("Nome deve ter entre 3 e 50 caracteres.")

        # Validação de email
        email = email_textfield.value.strip()
        if not email_textfield.value.strip():
            valid = False
            error_messages.append("Email é obrigatório")
        else:
            # Verificação se o email já está em uso
            existing_email = User.get_user_by_email(email)
            if existing_email:
                valid = False
                error_messages.append("Este email já está em uso")

        # Validação de senha
        password = password_textfield.value
        if len(password) < 8:
            valid = False
            error_messages.append("Sua senha deve ter no mínimo 8 caracteres")
        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            valid = False
            error_messages.append("Sua senha deve conter letras e números")

        # Validação de confirmação de senha
        if password != confirm_password_textfield.value:
            valid = False
            error_messages.append("As senhas não batem.")

        # Validação de altura
        try:
            height = float(height_textfield.value)
            if height <= 0:
                valid = False
                error_messages.append("Altura deve ser maior que zero")
        except ValueError:
            valid = False
            error_messages.append("Altura inválida (apenas números).")

        # Validação de peso
        try:
            weight = float(weight_textfield.value)
            if weight <= 0:
                valid = False
                error_messages.append("Peso deve ser maior que zero")
        except ValueError:
            valid = False
            error_messages.append("Peso inválido (apenas números).")

        # Validação do tipo sanguíneo
        blood = blood_type_dropdown.value
        if not blood:
            valid = False
            error_messages.append("Por favor, selecione um tipo sanguíneo.")

        # Validação de CPF
        cpf = cpf_textfield.value.strip()

        if not cpf.isdigit() or len(cpf) != 11:
            valid = False
            error_messages.append("CPF inválido (deve conter apenas 11 numeros)")
        else:
            # Verificação se o CPF já está cadastrado
            existing_cpf = User.get_user_by_cpf(cpf)
            if existing_cpf:
                valid = False
                error_messages.append("Este CPF já está cadastrado")

            # Validação de CPF usando a função validate_cpf
            if not validate_cpf(cpf):
                valid = False
                error_messages.append("CPF inválido.")

        # Validação da data de nascimento
        try:
            datetime.strptime(birth_textfield.value, "%d/%m/%Y")
        except ValueError:
            valid = False
            error_messages.append("Data de nascimento inválida (formato correto: DD/MM/YYYY).")

        # Validação de sexo
        sex = sex_dropdown.value
        if not sex:
            valid = False
            error_messages.append("Por favor, selecione um sexo.")

        # Validação de telefone
        phone = phone_textfield.value.strip()
        if not phone or len(phone) != 11:
            valid = False
            error_messages.append("Telefone inválido, deve conter 11 algarismos")

        if not valid:
            page.dialog = AlertDialog(
                content=Column(controls=[
                    Text("Erro no cadastro:", size=18, color=colors.RED),
                    *map(Text, error_messages),
                ]),
                actions=[
                    Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)
                ],
            )
            page.dialog.open = True
            page.update()
        else:
            User.add_users(name_textfield.value,
                           email_textfield.value,
                           cpf_textfield.value,
                           password_textfield.value,
                           birth_textfield.value,
                           sex_dropdown.value,
                           phone_textfield.value,
                           blood_type_dropdown.value,
                           height_textfield.value,
                           weight_textfield.value)
            page.go("/login")

    def format_date(e):
        pass

    name_textfield = TextField(label="Nome", width=315, filled=True, bgcolor=colors.WHITE)
    name_row = Row([name_textfield], alignment=MainAxisAlignment.CENTER)

    email_textfield = TextField(label="Email", width=315, filled=True, bgcolor=colors.WHITE)
    email_row = Row([email_textfield], alignment=MainAxisAlignment.CENTER)

    password_textfield = TextField(label="Senha", width=315, filled=True, bgcolor=colors.WHITE, password=True,
                                   can_reveal_password=True)
    password_row = Row([password_textfield], alignment=MainAxisAlignment.CENTER)

    confirm_password_textfield = TextField(label="Confirme a senha", width=315, filled=True, bgcolor=colors.WHITE,
                                           password=True, can_reveal_password=True)
    confirm_password_row = Row([confirm_password_textfield], alignment=MainAxisAlignment.CENTER)

    weight_textfield = TextField(label="Peso", width=60, filled=True, bgcolor=colors.WHITE,
                                 keyboard_type=KeyboardType.NUMBER, hint_text="kg")
    weight_row = Row([weight_textfield], alignment=MainAxisAlignment.CENTER)

    height_textfield = TextField(label="Altura", width=70, filled=True, bgcolor=colors.WHITE,
                                 keyboard_type=KeyboardType.NUMBER, hint_text="m")
    height_row = Row([height_textfield], alignment=MainAxisAlignment.CENTER)

    blood_type_dropdown = Dropdown(label="Tipo sanguíneo", width=165, options=[
        dropdown.Option("A+"),
        dropdown.Option("A-"),
        dropdown.Option("B+"),
        dropdown.Option("B-"),
        dropdown.Option("AB+"),
        dropdown.Option("AB-"),
        dropdown.Option("0+"),
        dropdown.Option("O-"),
        dropdown.Option("Não sei"),
    ])
    blood_type_dropdown_row = Row([blood_type_dropdown], alignment=MainAxisAlignment.CENTER)

    weight_height_blood_type_row = Row([weight_row, height_row, blood_type_dropdown_row],
                                       alignment=MainAxisAlignment.CENTER)

    cpf_textfield = TextField(label="CPF", width=315, filled=True, bgcolor=colors.WHITE,
                              keyboard_type=KeyboardType.NUMBER, hint_text="Apenas números")
    cpf_row = Row([cpf_textfield], alignment=MainAxisAlignment.CENTER)

    birth_textfield = TextField(label="Data de nascimento", width=190, filled=True, bgcolor=colors.WHITE,
                                hint_text="DD/MM/YYYY", on_change=format_date)
    birth_row = Row([birth_textfield], alignment=MainAxisAlignment.CENTER)

    sex_dropdown = Dropdown(label="Sexo", width=115, options=[
        dropdown.Option("Masculino"),
        dropdown.Option("Feminino")
    ])
    sex_dropdown_row = Row([sex_dropdown], alignment=MainAxisAlignment.CENTER)

    sex_birth_row = Row([birth_row, sex_dropdown_row], alignment=MainAxisAlignment.CENTER)

    phone_textfield = TextField(label="Telefone", width=315, filled=True, bgcolor=colors.WHITE,
                                hint_text="Apenas números")
    phone_row = Row([phone_textfield], alignment=MainAxisAlignment.CENTER)

    register_button = ElevatedButton(content=Text("Cadastrar", size=15), on_click=send_register,
                                     style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), width=140)
    register_button_row = Row([register_button], alignment=MainAxisAlignment.CENTER)

    def send_login(e):
        page.go("/login")

    content = Stack(
        [Column(
            [Text("", height=50),
             Row([IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED, on_click=send_login, icon_color=colors.BLACK,
                             icon_size=35),
                  Text("")],
                 alignment=MainAxisAlignment.SPACE_AROUND)]
        ),
            Column(controls=[Text("", height=60),
                             Row(controls=[Text("Cadastro", size=20, weight=FontWeight.W_700)],
                                 alignment=MainAxisAlignment.CENTER),
                             name_row,
                             email_row,
                             password_row,
                             confirm_password_row,
                             weight_height_blood_type_row,
                             cpf_row,
                             sex_birth_row,
                             phone_row,
                             register_button_row
                             ], alignment=MainAxisAlignment.CENTER)])

    return content
