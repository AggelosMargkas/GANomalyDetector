function [c] = 	psarakis_function(image)
    a = double(image);
    figure(1)

    %Pairnoume to size tou matrix ths eikonas
    s=size(a);

    %Midenizoume ola ta 255.
    a(a==255)=0;
    subplot(1,4,1);imagesc(a);title('Input image.');colormap(gray);
    %Paizoume mpala me ta rows afairontas ta prwta kai teletautai 100.
    a=a(700:end-200,:);
    %Plotaroume thn arxiki eikona.
    subplot(1,4,2);imagesc(a);title('First crop');colormap(gray);

    image_information_distribution = cumsum(sum(a')) ./ [1:length(sum(a'))]; %#ok<NBRAK,UDIM>

    %plot(image_information_distribution)

    difference_of_logarithm_of_information = diff(log10(image_information_distribution));

    sign_of_cumsum_of_differences = sign(cumsum(difference_of_logarithm_of_information));

    i=find(fliplr(sign_of_cumsum_of_differences)==-1); 

    if ~isempty(i)
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
end  