pipeline{
  environment {
    registry = "harbor.its.local/library/netvault_capacity"
    dockerImage = ""
  }

    agent any
    stages{
        stage("Check out git"){
            steps{
                echo "====++++git clone repository++++===="
                git 'https://github.com/teynakopha/NetvaultSingleTapeMailAlert'
            }
        }
        stage("build image"){
            steps{
                script{
                    dockerImage =  docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage("push image"){
            steps{
                script{
                    docker.withRegistry( "" ) {
                        dockerImage.push()
                    }
                }

            }
        }
        stage("deploy app"){
            steps{
                script{
                    kubernetesDeploy(configs: "NetvaultCheckCapa.yaml", kubeconfigId: "newkubeconfig")
                }
                
            }
        }

    }

}