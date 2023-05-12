package khan.translator.imgreader;

import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

public class ImgReader {
	
	public static void readTextFromImg() {
		
		
		try {
			
			Tesseract tesseract = new Tesseract();
						  
	        tesseract.setDatapath("/Users/meganthurston/Downloads/Tess4J/tessdata");
	
	        Path path = Paths.get("/Users/meganthurston/challenge-workspace/BengaliToEnglishTranslator/translator/img/banglaImg.jpeg");
	        File img = path.toFile();
	        String result = tesseract.doOCR(img);
            System.out.println(result);

		}
	    catch (TesseractException e) {
	        e.printStackTrace();
	    }
	}
	
}
