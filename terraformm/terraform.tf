resource "aws_instance" "my_ec2"{
   ami = "ami-0e83be366243f524a"
   instance_type = "t2.micro"
   key_name = "Cecilia_Aparicio"
   tags = {
     Name = "cecy"
   }
security_groups = [aws_security_group.my_security_groupcecy.id]
subnet_id = "subnet-04ce466f"

}

resource "aws_security_group" "my_security_groupcecy" {
  name        = "my_security_groupcecy"
  description = "Security group for SSH and HTTP access"
  vpc_id = "vpc-c2c3a2a9"
 
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  ingress {
    from_port   = 9090
    to_port     = 9090
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


egress {
 from_port   = 0
 to_port     = 0
 protocol    = "-1"
 cidr_blocks = ["0.0.0.0/0"]
}

}

