<br>

# 🛠️ [1931 회의실 배정](http://www.acmicpc.net/problem/1931) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/10.svg"/>

<br>

## 📖 문제
>한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

<br>

## ⌨️ 입력
>첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

<br>

## 💻 출력
>첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

<br><br>

<details>
  
  <summary> 
  
  ## 🎈 참고
  </summary>
  <br>

  ## 📄 로직
  
> 입력받은 회의시간을 <code>timetable</code>리스트에 저장 및 종료시간 오름차순 정렬(종료시간이 같다면 시작시간 오름차순 정렬)
> 
> 첫번째 회의 정보(회의 종료 시간) <code>result</code>리스트에 저장
> - 다른 회의와 비교하며 겹치지 않는 회의가 있다면 해당 회의 정보(회의 종료 시간)도 저장
>
> 모든 회의를 확인했다면 <code>result</code>리스트 항목 갯수(최대 가능 회의 수) 출력
>
> <br>
> 
> ### 비슷한 백준 문제
> - [11000 강의실 배정](https://github.com/jjjuni/CodingTest_py/tree/main/Baekjoon/gold/greedy/11000)

  

</details>

<br><br>
