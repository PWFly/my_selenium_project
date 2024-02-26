pipeline{

    environment{
        VIRTUAL_HOST = 'venv'
        PATH = "$VIRTUAL_HOST/bin:$PATH"
    }

    stage{
        stage('SetUp'){
            steps{
                echo "Setting up virtual environment..."
                sh 'python -m venv $VIRTUAL_ENV'
                sh 'source $VIRTUAL_ENV/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests'){
            steps{
                echo "Running tests..."
                sh 'pytest test'
            }
        }
    }

    post{
        success{
            echo "Test succeeded!"
        }
        failure{
            echo "Test failed!"
        }
        always{
            echo "Cleaning up virtual environment..."
            sh 'rm -rf $VIRTUAL_ENV'
        }
    }
}