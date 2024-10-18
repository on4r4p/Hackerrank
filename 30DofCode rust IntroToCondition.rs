use std::io;

fn main() {
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Erreur input");

    let n: usize = input.trim().parse()
        .expect("error usize");
    if n % 2 != 0 {
       println!("Weird"); 
    } else if n > 2 && n<= 5{
       println!("Not Weird");
    } else if n > 5 && n<= 20{
        println!("Weird");
    } else if n > 20 {
        println!("Not Weird");
    }
    
}
