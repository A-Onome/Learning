resource "local_file" "Second_file" {
    content = var.content
    filename = var.filename  
}