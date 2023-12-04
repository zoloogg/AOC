use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();

    let mut iterator = stdin.lock().lines();

    let line1 = iterator.next().unwrap().unwrap();

    let mut cnt = 0;
    let mut ans2: i16 = -1;

    for (i, c) in line1.chars().enumerate() {
        if c == '(' {
            cnt += 1;
        }
        else{
            cnt -= 1;
        }

        if cnt == -1 && ans2 == -1 {
            ans2 = i as i16 + 1;
        }
    }

    println!("part1: {}", cnt);
    println!("part2: {}", ans2);
}