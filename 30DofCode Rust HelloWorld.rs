use std::io;

fn main() {
    let mut input = String::new();
    
    io::stdin()
        .read_line(&mut input)
        .expect("Erreur");
    println!("Hello, World.");
    println!("{}", input.trim());
}
