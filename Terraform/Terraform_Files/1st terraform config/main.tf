resource "local_file" "First_file" {
    content = "This is my first config file"
    filename = "First file"
  
}

resource "random_pet" "test_pet" {
    prefix = "Mr"
    separator = "."
}