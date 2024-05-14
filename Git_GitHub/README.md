
# Primeiros Passos Git

Após instalarmos o Git em nossa máquina, é necessário fazermos algumas configurações.  
Deixarei aqui a documentação do Git caso precisem:

- [ **Git-Doc** 📃](https://git-scm.com/doc)

## Definindo nome do usuário:

Precisamos definir um nome de usuário para nosso Git, pois ele será exibido em cada alteração que fizermos em repositórios.

Exemplo: 

![Ex nome de user](https://i.imgur.com/kk04d6q.png)

Para fazer isso utilizamos o seguinte comando:  
**git config --global user.name "nome do usuario"**

git é usado em qualquer comando relacionado ao Git que você for fazer.  

config é usado sempre que você utilizar/definir uma configuração no seu git.  

--global se refere ao escopo, que é a que "nível" você está alterando essas configurações, 
podendo ser system, global, worktree, file e local. Normalmente utilizaremos o --global.  

user para acessarmos as configurações relacionadas ao usuário e  
name é uma função dentro de user que serve juntas servem para alterar seu nome de usuário.

![comando](https://i.imgur.com/zNRDbH1.png)

Após usarmos esse comando, executamos ele novamente para verificar se o nome do usuário está aparecendo corretamente: 

![repete comando](https://i.imgur.com/lovtcw9.png)  
![nome](https://i.imgur.com/rH9zWM9.png)

No meu caso em específico, por meu nome de usuário possuir caracteres especiais ele fica dessa forma, porém se o seu não possuir ele fica normal.

## Definindo email:

Similar ao passo anterior o email que definirmos irá aparecer em cada alteração que fizermos em um repositório.

**Indico fortimente que usem o mesmo email do GitHub nessa configuração.**

O comando utilizado para isso é:  
**git config --global user.email emailquedesejausar@skl.com**

A estrutura é extremamente similar ao comando anterior, só muda que invés de usarmos user.name usamos user.email, pois desejamos alterar o email.

![demonstração imagem](https://i.imgur.com/OAdRzUk.png)

Da mesma forma que o comando anterior, executamos novamente o comando, mas sem a alteração que queremos fazer:

![repete comando](https://i.imgur.com/q09oJ5o.png)  
![email](https://i.imgur.com/zdgGTKS.png)


## Modificando o nome padrão da Branch

Uma Branch funcionam como um controle de origem que permite trabalhar em um conjunto de alterações separado do código principal. Por exemplo, enquanto mantemos o código de produção na branch principal, podemos criar uma ramificação para trabalhar livremente neste código e somente depois juntar estes códigos.

Ao instalarmos o Git, o nome padrão definido para essas Branch é master, porém nos repositórios mais atuais usamos o termo main no lugar do master.

Para isso usamos o seguinte comando:  
**git config --global init.defaultBranch main**

Da mesma forma que os comandos anteriores, git, config e --global funcionam igual.  
Mas fomos apresentado a um novo termo, o init.  

init é utilizado no momento de criarmos um repositório, mas no caso desse comando que estamos vendo, ele está aí para definir que a partir do momento que você criar um repositório, o nome da Branch padrão será aquela que você definir.

![rename branch](https://i.imgur.com/Aka4bJh.png)

E usaremos o comando novamente para verificar se funcionou:

![repete comando](https://i.imgur.com/PFLl5wi.png)  
![branch name](https://i.imgur.com/L9tqTAi.png)

