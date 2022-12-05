% Specify the folder where the files live.
myFolder = "C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\comparison_full_mammos";

% Check to make sure that folder actually exists.  Warn user if it doesn't.
if ~isfolder(myFolder)
    errorMessage = sprintf('Error: The following folder does not exist:\n%s\nPlease specify a new folder.', myFolder);
    uiwait(warndlg(errorMessage));
    myFolder = uigetdir(); % Ask for a new one.
    if myFolder == 0
         % User clicked Cancel
         return;
    end
end

%Get all sub directories in comparison full mamograms.
subDirsNames = GetSubDirsFirstLevelOnly(myFolder);

% Get a list of all files in the folder with the desired file name pattern.
filePattern = fullfile(subDirsNames(1)); % Change to whatever pattern you need.

%filePattern = fullfile(myFolder, '*.jpg'); % Change to whatever pattern you need.
theFiles = dir(filePattern);

for i = 1 : length(subDirsNames)

    filePattern = fullfile(subDirsNames(i)); % Change to whatever pattern you need.
    theFile = dir(filePattern);
    
    [pathstr, name_base, ext] = fileparts(theFile(3).name);
    
    baseFileName = theFile(3).name;
    baseFilePath = theFile(3).folder;
    %fullImagePath = 'C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\data\jpeg\1.3.6.1.4.1.9590.100.1.2.257979549512926684716381871403745112147\1-107.jpg';
    fullImagePath = fullfile(baseFilePath, baseFileName);
    fprintf(1, 'Now reading %s\n', fullImagePath);
    
    % Now do whatever you want with this file name,
    % such as reading it in as an image array with imread()
    imageArray = imread(fullImagePath);
    c = cropping_images(imageArray);
    imagesc(c);title(baseFileName);colormap(gray);
%   imagesc(c);  % Display image.
    name = [baseFilePath, '\', name_base, '_Psarakis', ext];
    if ~isempty(c) 
        imwrite(c,gray,name)
    end
    drawnow; % Force display to update immediately.
end

%%%
%for k = 1 : length(theFiles)[0:1])
%    baseFileName = theFiles(3).name;
%    eFileName = theFiles(k).name;
%    fullImagePath = 'C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\data\jpeg\1.3.6.1.4.1.9590.100.1.2.257979549512926684716381871403745112147\1-107.jpg';
%    %fullImagePath = fullfile(theFiles(k).folder, baseFileName);
%    fprintf(1, 'Now reading %s\n', fullImagePath);
%    % Now do whatever you want with this file name,
%    % such as reading it in as an image array with imread()
%    imageArray = imread(fullImagePath);
%    %c = cropping_images(imageArray);
%    imagesc(imageArray);colormap(gray); % Display image.
%    drawnow; % Force display to update immediately.
%end
%%%

function [subDirsNames] = GetSubDirsFirstLevelOnly(parentDir)
% Get a list of all files and folders in this folder.
files    = dir(parentDir);
names    = {files.name};
% Get a logical vector that tells which is a directory.
dirFlags = [files.isdir] & ~strcmp(names, '.') & ~strcmp(names, '..');
% Extract only those that are directories.
subDirsNames = parentDir + '\' + names(dirFlags);
end

function c = cropping_images(image)
    a = double(image);
    figure(1)

    %Pairnoume to size tou matrix ths eikonas
    s=size(a);

    %Midenizoume ola ta 255.
    a(a==255)=0;
    %subplot(1,4,1);imagesc(a);title('Input image.');colormap(gray);
    %Paizoume mpala me ta rows afairontas ta prwta kai teletautai 100.
    a=a(100:end-100,100:end-100);
    %Plotaroume thn arxiki eikona.
    %subplot(1,4,2);imagesc(a);title('First crop');colormap(gray);

    image_information_distribution = cumsum(sum(a')) ./ [1:length(sum(a'))]; %#ok<NBRAK,UDIM>

    %plot(image_information_distribution)

    difference_of_logarithm_of_information = diff(log10(image_information_distribution));

    sign_of_cumsum_of_differences = sign(cumsum(difference_of_logarithm_of_information));

    i=find(fliplr(sign_of_cumsum_of_differences)==-1); 

    if ~isempty(i)& i>=500
        b=a(1:i(1),:);
        fprintf('Bottom point found => %d \n', i(1))
    else
        b=a;
        fprintf('Failed to cut the bottom because point of interest i is empthy \n')
    end

    %subplot(1,4,3);imagesc(b);title('Bottom wise crop.');colormap(gray);

    j=find(diff(fliplr(sign(diff(cumsum((sum(b)))./[1:length(sum(b))]))))==-2); %#ok<NBRAK>

    if ~isempty(j)
        c=b(:,s(2)-j(1):end);
        fprintf('Left point found => %d \n', j(1))
    else
        c=b;
        fprintf('Failed to cut the top bc is empty \n')
    end

    %subplot(1,4,4);
    %imagesc(c);title('Left or right wise crop.');colormap(gray);
    
    
end  