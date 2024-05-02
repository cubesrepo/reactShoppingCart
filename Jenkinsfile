pipeline{
    agent any
    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/reactShoppingCart.git'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv reactShoppingCartVENV'
                bat 'reactShoppingCartVENV\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'reactShoppingCartVENV\\Scripts\\activate && pytest -v --html=report.html'
            }
        }
    }
}