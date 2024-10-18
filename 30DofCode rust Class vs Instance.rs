

impl Person {
    fn new(initialAge: i32) -> Person {

        let age = if initialAge < 1{
            println!("Age is not valid, setting age to 0.");
            0
        } else {
            initialAge
        };
        return Person { age: initialAge };
        
    }
 
    fn amIOld(&self) {
        // Do some computations in here and print out the correct statement to the console
        if self.age < 13{
            println!("You are young.")
        } else if self.age >= 13 && self.age <18{
            println!("You are a teenager.")
        }else{
            println!("You are old.")
        }
        
    }
 
    fn yearPasses(&mut self) {
        // Increment the age of the person in here
        self.age += 1
    }
}

