
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "app_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "app_vpc"
  }
}

resource "aws_subnet" "app_subnet" {
  cidr_block = "10.0.1.0/24"
  vpc_id = aws_vpc.app_vpc.id
  availability_zone = "us-east-1a"
  tags = {
    Name = "app_subnet"
  }
}

resource "aws_security_group" "app_sg" {
  name = "app_sg"
  vpc_id = aws_vpc.app_vpc.id
  
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "app_keypair" {
  key_name   = "app_keypair"
  public_key = file("~/.ssh/app_keypair.pub")
}

resource "aws_instance" "app_instance" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.app_subnet.id
  security_groups = [aws_security_group.app_sg.id]
  key_name = aws_key_pair.app_keypair.key_name
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World!" > index.html
              nohup python3 /app/app.py &
              EOF
  tags = {
    Name = "app_instance"
  }
}

resource "aws_lb" "app_lb" {
  name = "app_lb"
  internal = false
  load_balancer_type = "application"
  security_groups = [aws_security_group.app_sg.id]
  subnets = [aws_subnet.app_subnet.id]
}


resource "aws_lb_target_group" "app_tg" {
  name = "app_tg"
  port = 80
  protocol = "HTTP"
  vpc_id = aws_vpc.app_vpc.id
  
  health_check {
    path = "/"
    protocol = "HTTP"
    timeout = 5
    interval = 10
    healthy_threshold = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_target_group_attachment" "app_tg_attach" {
  target_group_arn = aws_lb_target_group.app_tg.arn
  target_id = aws_instance.app_instance.id
  port = 80
}

resource "aws_lb_listener" "app_lb_listener" {
  load_balancer
