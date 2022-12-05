close

% find(X)
% Returns the linear indeces(indexes) of each nonzero element in array X.

% fliplr(A)
% Return A with its columns flipped in the left-right direction.
% A = 1:10 (1 2 3 4 5 6 7 8 9 10)
% B = fliplr(A)
% B = (10 9 8 7 6 5 4 3 2 1)

% Y = sign(x)returns an array Y the same size as x, where each elemnt of Y
% is:
% + 1 if the corresponding element of x is greater than 0.
% + 0 if the corresponding element of x equals 0.
% + -1 if the corresponding element of x is less than 0.

% B = cumsum(A)
% Returns the cumulative sum of A starting at the beginning of the first
% array, whose size does not equal to 1.
%
% A cumulative sum is a sequence of partial sums of a given sequence.

% Y diff(X) calculates the differences between adjacent elements of X along
% the first array dimension.
%
% If X is a vector of length m, then the diff() will return a vector of
% length m-1. The retourned elements will be the differences of the
% adjacent elements of X.
%
% If X is a nonempty, nonvector p X m matrix, then the diff() will return a
% matrix of size (p-1) X m, whose elements are the differences between the
% rows of x.

% If A is a matrix, then sum(A) returns a row vector containing the sum of each column.

% Pairnoume olo to cumulative sum tou sum olwn ton column ths eikonas. Auto
% to kanoume transpose, pou simainei oti einai row.
% Kai meta auto to diairoume me to length to A transpose.

% Auto mas dinei to mean value ana pixel thn eikonas se ena dianisma
% 1 x (number of rows.)


%bad example
%a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\fullMammogramsConvertedToPng\1-299.jpg');

%antother example, noise on top.
%a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\data\jpeg\1.3.6.1.4.1.9590.100.1.2.425182509912779827704955040293854758529\1-022.jpg');

%problematic example bottomwise pixels does not work properly. AND leftmost
%wish works reversly.
%a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\data\jpeg\1.3.6.1.4.1.9590.100.1.2.307271664512650974022213502811472047069\1-201.jpg');

% Good example, we lose some information on the bottom of the image.
%a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\data\jpeg\1.3.6.1.4.1.9590.100.1.2.257979549512926684716381871403745112147\1-107.jpg');

% Let's go.
%a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\comparison_full_mammos\1-000\1-000.jpg');

% Horrible example, but fixed with if args on the first cut.
%a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\comparison_full_mammos\1-009\1-009.jpg');

% Let's go.
a = imread('C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\VINDR_MAMMOGRAM.png');

%a = alpha;
%a = double(a);
figure(1)

%Pairnoume to size tou matrix ths eikonas
s=size(a);

%Midenizoume ola ta 255.
a(a==255)=0;
subplot(1,4,1);imagesc(a);title('Input image.');colormap(gray);
%Paizoume mpala me ta rows afairontas ta prwta kai teletautai 100.
a=a(100:end-100,100:end-100);
%Plotaroume thn arxiki eikona.
subplot(1,4,2);imagesc(a);title('First crop');colormap(gray);

image_information_distribution = cumsum(sum(a')) ./ [1:length(sum(a'))]; %#ok<NBRAK,UDIM>

%plot(image_information_distribution)

difference_of_logarithm_of_information = diff(log10(image_information_distribution));

sign_of_cumsum_of_differences = sign(cumsum(difference_of_logarithm_of_information));

i=find((sign_of_cumsum_of_differences)==-1); 
%i=find(fliplr(sign_of_cumsum_of_differences)==-1); 

if ~isempty(i) & i >= 500
    b=a(1:i(1),:);
    fprintf('Bottom point found => %d \n', i(1))
else
    b=a;
    fprintf('Failed to cut the bottom because point of interest i is empthy \n')
end

subplot(1,4,3);imagesc(b);title('Bottom wise crop.');colormap(gray);

j=find(diff(fliplr(sign(diff(cumsum((sum(b)))./[1:length(sum(b))]))))==-2); %#ok<NBRAK>

if ~isempty(j)
    c=b(:,s(2)-j(1):end);
    fprintf('Left point found => %d \n', j(1))
else
    c=b;
    fprintf('Failed to cut the top bc is empty \n')
end

subplot(1,4,4);imagesc(c);title('Left or right wise crop.');colormap(gray);