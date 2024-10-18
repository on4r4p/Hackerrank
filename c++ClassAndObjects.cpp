#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

struct Student{
    vector<int>scores;

    void input(){
        int score;
        for (int i = 0; i < 5; i++) {
        cin >> score;
        scores.push_back(score);}
        
    }
    int calculateTotalScore()const{
        int sum= 0;
        for(int i = 0; i < 5; i++){
            sum += scores[i];
        }
        return sum;
    }


//    string to_string() const {
 //       return ::to_string(age)+","+first_name+","+last_name+","+::to_string(standard);
 //   }
};

int main() {
    int n; // number of students
    cin >> n;
    Student *s = new Student[n]; // an array of n students
    
    for(int i = 0; i < n; i++){
        s[i].input();
    }

    // calculate kristen's score
    int kristen_score = s[0].calculateTotalScore();

    // determine how many students scored higher than kristen
    int count = 0; 
    for(int i = 1; i < n; i++){
        int total = s[i].calculateTotalScore();
        if(total > kristen_score){
            count++;
        }
    }

    // print result
    cout << count;
    
    return 0;
}
