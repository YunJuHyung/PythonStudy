"""정렬된 숫자 리스트(num_list)와 찾고자 하는 요소(element)가 주어졌을 때, 이진 탐색 알고리즘을 사용하여 요소가 리스트의 몇 번째 인덱스에 위치하는지 반환하는 함수를 작성하고, 해당 함수를 사용하여 num_list에서 element 7을 찾을 때의 결과를 출력하는 문제를 만들 수 있습니다."""

def binary_search(element, num_list):
  left = 0
  right = len(num_list) - 1
  answer = 0

  while left <= right:
    middle = (left + right) // 2
    if num_list[middle] == element:
      answer = middle
      break
    if middle < element:
      left = middle + 1
    elif middle > element:
      right = middle - 1
  return answer


num_list = [1, 3, 5, 7, 9]
element = 7
print(binary_search(element, num_list)) 