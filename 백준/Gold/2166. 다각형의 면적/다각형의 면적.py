# outer product
# A = [a, b], B = [c, d]
# A X B = |A| * |B| sin(theta) = ad - bc
# 1/2 * |A| * |B| sin(theta) = 1/2(ad - bc)

def outer_product(A, B):
    # A = [a, b], B = [c, d]
    return 1/2*(A[0]*B[1] - A[1]*B[0])

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

start = points[0]

answer = float(0)
for i in range(1, N-1):
    A = [points[i][0] - start[0], points[i][1] - start[1]]
    B = [points[i+1][0] - start[0], points[i+1][1] - start[1]]
    answer += outer_product(A, B)

print(f'{abs(answer):.1f}')
    